import pandas as pd
from rest_framework import permissions, status, viewsets
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FileUploadAPI
from .serializers import FileUploadAPISerializer


class FileUploadAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileUploadAPISerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # permission_classes = [permissions.AllowAny]

    # def put(self, request, filename, format=None):
    #     try:
    #         file_obj = request.data["file"]
    #         file_content = file_obj.read()
    #         df = pd.read_excel(file_content, engine="openpyxl")
    #         return Response({"status": "success", "message": "File uploaded."})
    #     except Exception as e:
    #         return Response({"status": "error", "message": str(e)})
