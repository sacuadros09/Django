from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tasks
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request) :
    return render (request,"about.html")


def hello(request,username) :
    return HttpResponse ("<h1>Hello %s</h1>" % username)

def projects(request):
    projects= list(Project.objects.values())
    return render (request,"projects.html")

def tasks(request):
   # tasks= get_object_or_404(Tasks, title=title)
    return render (request,"tasks.html")