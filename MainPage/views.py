import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render
from .models import UploadedFiles
from .txtProcess import process_uploaded_files

def mainPage(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')

        for file in uploaded_files:
            UploadedFiles.objects.create(file=file)
            logger.warning(f' [INFO] Uploaded {file.name}')
            process_uploaded_files()

            return render(request, 'MainPage.html')


    return render(request, "MainPage.html")