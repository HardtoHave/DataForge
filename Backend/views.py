from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataFile
from .serializers import DataFileSerializer
from .infer_data_types import infer_and_convert_data_types
import pandas as pd


class DataFileUploadedView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        data_file = DataFile.objects.create(file=file)
        df = pd.read_csv(data_file.file.path)
        df = infer_and_convert_data_types(df)
        data_file.data_types = df.dtypes.todict()
        data_file.processed = True
        data_file.save()

        serializer = DataFileSerializer(data_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DataFileListView(APIView):
    def get(self, request):
        data_files = DataFile.objects.all()
        serializer = DataFileSerializer(data_files, many=True)
        return Response(serializer.data)
