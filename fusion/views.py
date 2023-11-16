from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd

from .models import ExcelFile

# def export_data_to_excel(request):
#     objs = ExcelFile.objects.all()
#     data = []
#     for obj in objs:
#         data.append(
#             {
#                 "file": obj.file,
#                 "uploaded_on": obj.uploaded_on,
#                 "description": obj.description,
#             }
#         )
#     pd.DataFrame(data).to_excel("output.xlsx")
#     return JsonResponse({"status": 200})


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
