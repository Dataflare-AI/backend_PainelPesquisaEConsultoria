import pandas as pd
from rest_framework import permissions, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = [permissions.AllowAny]

    def put(self, request, filename, format=None):
        try:
            file_obj = request.data["file"]
            file_content = file_obj.read()
            df = pd.read_excel(file_content, engine="openpyxl")
            return Response({"status": "success", "message": "File uploaded."})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})
