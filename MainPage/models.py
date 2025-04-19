from django.db import models

class UploadedFiles(models.Model):
    file = models.FileField(unique=True, upload_to='txts')
    tf = models.FloatField(blank=True,null=True)
    idf = models.FloatField(blank=True,null=True)
