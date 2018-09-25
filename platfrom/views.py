import json
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from PlatformModel.models import TestObjects
from .dataloader import dataloader
from . import values


def index(request):
    return render(request, "index.html", {})
    # return render_to_response('index.html')
