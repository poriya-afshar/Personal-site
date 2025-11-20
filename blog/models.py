from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
import random
import string


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(unique=True, blank=True, max_length=200, verbose_name="اسلاگ")
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True, verbose_name="تصویر")
    content = models.TextField(verbose_name="محتوا")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    author = models.CharField(max_length=100, default="ناشناس", verbose_name="نویسنده")

    class Meta:
        verbose_name = "پست وبلاگ"
        verbose_name_plural = "پست‌های وبلاگ"
        ordering = ['-created_at']

    def generate_unique_slug(self):
        """تولید slug یونیک"""
        # اگر عنوان فارسی بود، از unidecode استفاده کن
        try:
            base_slug = slugify(unidecode(self.title))
        except:
            base_slug = slugify(self.title)

        # اگر slug خالی شد (مثلاً فقط فارسی بود)، از id و رندوم استفاده کن
        if not base_slug:
            random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            base_slug = f"post-{random_str}"

        slug = base_slug
        counter = 1

        # بررسی یونیک بودن
        while BlogPost.objects.filter(slug=slug).exclude(id=self.id).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, verbose_name="نام")
#     email = models.EmailField(verbose_name="ایمیل")
#     text = models.TextField(verbose_name="متن نظر")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
#
#     class Meta:
#         verbose_name = "نظر"
#         verbose_name_plural = "نظرات"
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return f"{self.name} - {self.post.title}"



class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)

    # ⬅️ این فیلد جدید اضافه شده
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="متن نظر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        ordering = ['created_at']  # ترتیب از قدیم به جدید تا ریپلای درست بیاد

    def __str__(self):
        return f"{self.name} - {self.post.title}"

    @property
    def is_reply(self):
        return self.parent is not None
