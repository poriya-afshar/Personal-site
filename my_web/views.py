from django.shortcuts import render
from project.models import Project
from footer.models import Footer,Form


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        Form.objects.create(name=name, email=email, massage=massage)

    project = Project.objects.all()
    footer = Footer.objects.all().last()
    return render(request,'index.html',context={'project':project,'footer':footer})


def single_blog(request):
    footer = Footer.objects.all().last()
    return render(request, 'single-blog.html',context={'footer':footer})
