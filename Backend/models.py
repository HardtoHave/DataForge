from django.db import models


class DataFile(models.Model):
    file = models.FileField(upload_to='data_files')
    processed = models.BooleanField(default=False)
    data_types = models.JSONField(null=True, blank=True)
