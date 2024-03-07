from django.urls import path
from . import views
urlpatterns = [
path('UploadFile', views.UploadFile, name='UploadFile'),
path('list_files', views.list_files, name='list_files'),
]