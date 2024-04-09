import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .infer_data_types import infer_and_convert_data_types
from .models import DataFile
from .serializers import DataFileSerializer


class DataFileUploadedView(APIView):
    def post(self, request):
        data_file = request.FILES.get('file')
        if not data_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an instance of DataFile with the uploaded file
        data_file_instance = DataFile.objects.create(file=data_file)
        try:
            # Read the file into a pandas DataFrame
            df = pd.read_csv(data_file_instance.file.path)
        except Exception as e:
            # If reading the file fails, return an error response
            return Response({'error': f'Failed to read uploaded file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Process the DataFrame to infer and convert data types
        df_processed = infer_and_convert_data_types(df)

        # Convert pandas dtypes to a JSON-serializable dict
        dtypes_dict = {col: str(df_processed[col].dtype) for col in df_processed.columns}

        # Serialize the dtypes dict to a JSON string and save to the DataFile instance
        data_file_instance.data_types = dtypes_dict
        data_file_instance.processed = True
        data_file_instance.save()

        # Serialize the DataFile instance to return as a response
        serializer = DataFileSerializer(data_file_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class DataFileListView(APIView):
    def get(self, request):
        data_files = DataFile.objects.filter(processed=True)
        serializer = DataFileSerializer(data_files, many=True)
        return Response(serializer.data)