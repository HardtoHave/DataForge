from rest_framework import serializers
from models import DataFile


class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFile
        fields = ['id', 'file', 'processed', 'data_types']
