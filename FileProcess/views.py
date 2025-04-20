import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render
from .models import UploadedFiles
from .txtProcess import process_txt
from django.http.response import HttpResponseRedirect, JsonResponse


def uploadPage(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')

        for file in uploaded_files:
            UploadedFiles.objects.create(file=file)
        return HttpResponseRedirect('/results')


    return render(request, "uploadPage.html", {'uploaded':UploadedFiles.objects.all()})

def results(request):
    if UploadedFiles.objects.all().count() != 0:
        result_table = process_txt()
        result_table_html = result_table.to_html()

        return render(request, 'results.html', {'results': result_table_html})
    else:
        return render(request, 'results.html')

def delete_file(request, file_id):
    try:
        file = UploadedFiles.objects.get(id=file_id)
        file.file.delete()
        file.delete()
        return JsonResponse({'status': 'success'},status=200)
    except UploadedFiles.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)