import os
import imghdr
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .functions import reading_a_file, sentence_parsing
import json

from pathlib import Path

def index(request):
    return render(request, 'staticfiles/index.html')

def dependency(request):
    return render(request, 'dependency.html')

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        filename = uploaded_file.name
        file_format = imghdr.what(uploaded_file)
        if file_format:
            filename = os.path.splitext(filename)[0] + '.' + file_format
        with open('C:\\Users\\Radzivill\\Desktop\\Homework\\NLIIS\\Лаб №1\\EYAZIS_2_2\\EYAZIS_2_2\\EYAZIS\\Project_2\\' + filename, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return JsonResponse({'text_file': reading_a_file(filename)})
    else:
        return JsonResponse({'status': 'fail'})

@csrf_exempt
def upload_text(request):
    if request.method == 'POST': 
        data = json.loads(request.body)
        sentence_parsing(data["span_text"])
        return JsonResponse({"status": 'True'})
    return JsonResponse({'status': 'False'})