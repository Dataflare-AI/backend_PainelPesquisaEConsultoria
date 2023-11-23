# views.py
import os
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from .models import ExcelFile
from .serializers import ExcelFileSerializer
from urllib.parse import urljoin


class ExcelExportAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        excel_files = ExcelFile.objects.all()
        serializer = ExcelFileSerializer(excel_files, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if "file" not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES["file"]
        obj = ExcelFile.objects.create(file=file)
        path = str(obj.file.path)

        try:
            df = pd.read_excel(path)

            # Processar e salvar os dados no banco de dados
            imported_data_list = []
            for index, row in df.iterrows():
                imported_data = {}
                for column_name, column_value in row.items():
                    imported_data[column_name] = column_value

                imported_data_list.append(imported_data)

            serializer = ExcelFileSerializer(data=imported_data_list, many=True)
            if serializer.is_valid():
                serializer.save()

                # Correção dos URLs
                base_url = request.build_absolute_uri("/")[:-1]  # Remover a barra no final
                file_url = obj.file.url
                full_url = urljoin(base_url, file_url)

                return Response(
                    {"status": "success", "data": serializer.data, "file_url": full_url}, status=status.HTTP_200_OK
                )
            else:
                return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
