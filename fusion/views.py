# views.py
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ExcelFile
from .serializers import ExcelFileSerializer


class ExcelImportAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        files = ExcelFile.objects.all()
        serializer = ExcelFileSerializer(files, many=True)
        return Response({"files": serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = ExcelFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            file_instance = serializer.instance
            file_instance.save_data_from_excel()  # Processar os dados do Excel

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
