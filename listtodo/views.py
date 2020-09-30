from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "listtodo/index.html")

def add_task(request):
    return render(request, "listtodo/add_task.html")