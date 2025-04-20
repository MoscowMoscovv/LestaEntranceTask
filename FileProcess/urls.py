from django.contrib import admin
from django.urls import path
from FileProcess.views import uploadPage, results, delete_file

urlpatterns = [
    path('', uploadPage, name='mainPage'),
    path('results', results, name='result'),
    path('delete-file/<int:file_id>/', delete_file, name='delete_file'),
]
