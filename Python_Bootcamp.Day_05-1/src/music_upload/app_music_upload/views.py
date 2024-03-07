from os import listdir
from os.path import isfile, join
import mimetypes

from django.shortcuts import render, HttpResponse
from django.conf import settings
import json  # Add this import for JSON serialization

from django.http import JsonResponse
# Create your views here.


from .forms import BlogForm

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def UploadFile(request):    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = BlogForm()

    media_path = settings.MEDIA_ROOT
    myfiles = [f for f in listdir(
        media_path + "/documents/") if isfile(join(media_path + "/documents/", f))]
    context = {'form': form, 'myfiles': myfiles}

    return render(request, 'upload.html', context)


def list_files(request):
    media_path = settings.MEDIA_ROOT
    myfiles = [f for f in listdir(
        media_path + "/documents/") if isfile(join(media_path + "/documents/", f))]

    # Return JSON response with the list of files
    return JsonResponse({'files': myfiles})
