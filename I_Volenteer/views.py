from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def hello():
  return HttpResponse('Hello World')
