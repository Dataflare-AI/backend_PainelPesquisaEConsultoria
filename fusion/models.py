from django.db import models


class FileUploadAPI(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        # return self.uploaded_on.date()
        return f"{self.file.name} uploaded on {self.uploaded_on.date()}"
