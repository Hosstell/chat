from django.http import HttpResponse
from django.template import Context, loader

from backend.backend.settings import BASE_DIR
import os
from django.shortcuts import render


def index(request):
    # template = loader.get_template(path)
    # return HttpResponse(template.render())
    return render(request, template_name='index.html')