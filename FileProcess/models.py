import os

from django.db import models

class UploadedFiles(models.Model):
    file = models.FileField(upload_to='txts',unique=True)
    tfidf = models.JSONField(default=dict)
