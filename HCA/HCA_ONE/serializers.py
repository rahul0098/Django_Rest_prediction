from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import imagedb

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model=imagedb
        fields = '__all__'


class UserCreationSerializer(serializers.ModelSerializer):
    print("mail class")
    email=serializers.EmailField(required=True,
                validators=[UniqueValidator(queryset=User.objects.all())]
                            )

    username=serializers.CharField(required=True,
                validators=[UniqueValidator(queryset=User.objects.all())]
                            )

    password=serializers.CharField(min_length=8)
    

    def create(self,validate_data):
        print("create is executed")
        user=User.objects.create_user(validate_data['username'], validate_data['email'],
             validate_data['password'])
        return user

    class Meta():
        model=User
        print("class is exexutes meta")
        fields=('id','username','password','email')


