from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import FileSerializer,UserCreationSerializer

from .prediction import  prediction

class FileView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self,request,*args,**kwargs):

        file_serializer=FileSerializer(data=request.data)

        if(file_serializer.is_valid()):
            file_serializer.save()
            file_serializer.data
            path=file_serializer.data['file']
            
            return Response((file_serializer.data,{'result':prediction(path)}),status=status.HTTP_201_CREATED)
        else:

            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForUserCreationView(APIView):
    def post(self,request):
        usercreation=UserCreationSerializer(data=request.data)
        if(usercreation.is_valid()):
            usercreation.save()
            return Response(usercreation.data,status=status.HTTP_201_CREATED)
        else:
            return Response(usercreation.errors,status=status.HTTP_400_BAD_REQUEST)




