from django.shortcuts import render
from footer.models import Footer, Form
from my_resume.models import SiteInfo, Skill, Experience, Project, Education
from blog.models import BlogPost
from Task.models import Task


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        Form.objects.create(name=name, email=email, massage=massage)

    tasks = Task.objects.all()
    footer = Footer.objects.all().last()
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:4]
    context = {
        'footer': footer,
        'latest_posts': latest_posts,
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


def single_blog(request):
    footer = Footer.objects.all().last()
    return render(request, 'single-blog.html', context={'footer': footer})


def resume(request):
    site_info = SiteInfo.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    educations = Education.objects.all()
    context = {
        'site': site_info,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'educations': educations,
    }
    return render(request, 'my_resume.html', context)
