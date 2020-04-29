from rest_framework import serializers

from .models import imagedb

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model=imagedb
        fields = '__all__'
