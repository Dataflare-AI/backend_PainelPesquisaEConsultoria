from django.db import models


def seed_db(n):
    for i in range(0, n):
        FileUploadAPI.objects.create(
            file=f"file_{i}",
            description=f"file_{i}",
        )


class FileUploadAPI(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.uploaded_on.date()
        # return f"{self.file.} uploaded on {self.uploaded_on.date()}"


class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")
