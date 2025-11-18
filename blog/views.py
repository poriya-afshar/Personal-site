from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost, Comment
from footer.models import Footer


def blog_list(request):
    """نمایش لیست تمام پست‌های وبلاگ"""
    posts = BlogPost.objects.all().order_by('-created_at')
    footer = Footer.objects.last()  # بهتر از .all().last()

    context = {
        'posts': posts,
        'footer': footer,
    }
    return render(request, 'blog-list.html', context)


def blog_detail(request, slug):
    """نمایش جزئیات یک پست"""
    post = get_object_or_404(BlogPost, slug=slug)
    footer = Footer.objects.last()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        text = request.POST.get("text", "").strip()

        if name and email and text:
            Comment.objects.create(
                post=post,
                name=name,
                email=email,
                text=text
            )
            messages.success(request, "نظر شما با موفقیت ثبت شد!")
            return redirect('blog_detail', slug=post.slug)
        else:
            messages.error(request, "لطفاً تمام فیلدها را پر کنید.")

    context = {
        'post': post,
        'footer': footer,
    }
    return render(request, 'single-blog.html', context)