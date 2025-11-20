from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost, Comment
from footer.models import Footer


#
# def blog_list(request):
#     """نمایش لیست تمام پست‌های وبلاگ"""
#     posts = BlogPost.objects.all().order_by('-created_at')
#     footer = Footer.objects.last()  # بهتر از .all().last()
#
#     context = {
#         'posts': posts,
#         'footer': footer,
#     }
#     return render(request, 'blog-list.html', context)
#
#
# def blog_detail(request, slug):
#     """نمایش جزئیات یک پست"""
#     post = get_object_or_404(BlogPost, slug=slug)
#     footer = Footer.objects.last()
#
#     if request.method == "POST":
#         name = request.POST.get("name", "").strip()
#         email = request.POST.get("email", "").strip()
#         text = request.POST.get("text", "").strip()
#
#         if name and email and text:
#             Comment.objects.create(
#                 post=post,
#                 name=name,
#                 email=email,
#                 text=text
#             )
#             messages.success(request, "نظر شما با موفقیت ثبت شد!")
#             return redirect('blog_detail', slug=post.slug)
#         else:
#             messages.error(request, "لطفاً تمام فیلدها را پر کنید.")
#
#     context = {
#         'post': post,
#         'footer': footer,
#     }
#     return render(request, 'single-blog.html', context)


def blog_list(request):
    """نمایش لیست تمام پست‌های وبلاگ"""
    posts = BlogPost.objects.all().order_by('-created_at')
    footer = Footer.objects.last()  # گرفتن آخرین فوتر

    context = {
        'posts': posts,
        'footer': footer,
    }
    return render(request, 'blog-list.html', context)


# views.py

def blog_detail(request, slug):
    """نمایش صفحه جزئیات پست + مدیریت ارسال نظر و پاسخ"""
    post = get_object_or_404(BlogPost, slug=slug)
    footer = Footer.objects.last()

    # تغییر مهم: فقط نظرات اصلی (بدون والد) را به تمپلیت می‌فرستیم.
    # پاسخ‌ها را در تمپلیت از طریق comment.replies.all می‌گیریم.
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        text = request.POST.get("text", "").strip()
        parent_id = request.POST.get("parent_id")  # دریافت آیدی والد در صورت وجود

        if name and email and text:
            parent_obj = None
            # اگر parent_id وجود داشت، یعنی این یک پاسخ است
            if parent_id:
                try:
                    parent_obj = Comment.objects.get(id=parent_id)
                except Comment.DoesNotExist:
                    parent_obj = None

            Comment.objects.create(
                post=post,
                parent=parent_obj,  # ذخیره رابطه پدر-فرزندی
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
        'comments': comments,  # ارسال لیست اصلاح شده
        'footer': footer,
    }
    return render(request, 'single-blog.html', context)
