import logging
from MainPage.models import UploadedFiles
logger = logging.getLogger(__name__)

def process_uploaded_files():
    rows = UploadedFiles.objects.all()
    text_files = [file.file.path for file in rows]
    # logging.warning(f' got txts: {text_files} ')