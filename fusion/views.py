from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ExcelFile, FileUploadAPI
from .serializers import FileUploadAPISerializer


def export_data_to_excel(request):
    objs = FileUploadAPI.objects.all()
    data = []
    for obj in objs:
        data.append(
            {
                "file": obj.file,
                "uploaded_on": obj.uploaded_on,
                "description": obj.description,
            }
        )
    pd.DataFrame(data).to_excel("output.xlsx")
    return JsonResponse({"status": 200})


def import_data_to_excel(request):
    if request.method == "POST":
        file = request.FILES["file"]
        obj = ExcelFile.objects.create(file=file)
        path = str(obj.file)
        print(f"{settings.BASE_DIR}/{path}")
        df = pd.read_excel(path)
        for d in df.values:
            print(d)
    return render(request, "excel.html")


class FileUploadAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileUploadAPISerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
