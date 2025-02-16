from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Tasks
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse("Index Page")

def hello(request,username) :
    return HttpResponse ("<h1>Hello %s</h1>" % username)

def about(request) :
    return HttpResponse ("<h2>About</h2>")

def projects(request):
    projects= list(Project.objects.values())
    return JsonResponse(projects,safe=False)

def tasks(request, title):
    tasks= get_object_or_404(Tasks, title=title)
    return HttpResponse("tasks: %s"%tasks.title)