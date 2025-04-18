from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

#from somewhere import handle_uploaded_file


def mainPage(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')  # name="files" в input

        saved_files = []

        for file in uploaded_files:
            filename = default_storage.save(file.name, file)  # сохраняем
            saved_files.append(filename)

        # Можно передать список файлов обратно в шаблон
        #return render(request, 'MainPage.html', {'saved_files': saved_files})

    return render(request, "MainPage.html")