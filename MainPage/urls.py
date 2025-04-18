from django.contrib import admin
from django.urls import path
from MainPage.views import mainPage

urlpatterns = [
    path('', mainPage, name='mainPage'),
]
