from rest_framework import serializers

from .models import FileUploadAPI


class FileUploadAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploadAPI
        fields = (
            "file",
            "uploaded_on",
        )
