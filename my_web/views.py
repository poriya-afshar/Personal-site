from django.shortcuts import render
from project.models import Project


def home(request):
    project = Project.objects.all()

    return render(request,'index.html',context={'project':project})


