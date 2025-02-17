from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tasks
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    title = "Django Course!!"
    return render(request,"index.html", {
        "title":title
    })

def about(request) :
    username= "Santiago Cuadros"
    return render (request,"about.html",{
        "username":username
    })



def hello(request,username) :
    return HttpResponse ("<h1>Hello %s</h1>" % username)

def projects(request):
    #projects= list(Project.objects.values())
    projects = Project.objects.all()
    return render (request,"projects.html",{
        "projects":projects
    })


def tasks(request):
   # tasks= get_object_or_404(Tasks, title=title)
   tasks=Tasks.objects.all()
   return render(request,"tasks.html",{
       "tasks":tasks
   })