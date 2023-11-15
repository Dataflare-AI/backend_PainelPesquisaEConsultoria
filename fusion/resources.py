from import_export import resources

from .models import FileUploadAPI


class FileUploadAPIResource(resources.ModelResource):
    class Meta:
        model = FileUploadAPI
        # fields = ('file', 'uploaded_on', 'description')
        # export_order = ('file', 'uploaded_on', 'description')
