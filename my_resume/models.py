from django.db import models



class SiteInfo(models.Model):
    # برای اطلاعات عمومی صفحه (singleton-ish)
    full_name = models.CharField(max_length=200, verbose_name="نام کامل")
    title = models.CharField(max_length=200, verbose_name="عنوان/تیتری کوتاه")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=50, verbose_name="تلفن")
    github = models.URLField(blank=True, verbose_name="GitHub")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    about = models.TextField(blank=True, verbose_name="درباره من")
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True, verbose_name="عکس پروفایل")
    header_bg = models.CharField(max_length=200, blank=True, verbose_name="گرادیان هدر (اختیاری)")

    class Meta:
        verbose_name = "اطلاعات سایت"
        verbose_name_plural = "اطلاعات سایت"

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام مهارت")
    level = models.PositiveSmallIntegerField(default=50, verbose_name="درصد تسلط (0-100)")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        ordering = ['order']
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"

    def __str__(self):
        return f"{self.name} ({self.level}%)"

class Experience(models.Model):
    job_title = models.CharField(max_length=200, verbose_name="عنوان شغلی")
    company = models.CharField(max_length=200, verbose_name="شرکت")
    start_year = models.CharField(max_length=20, verbose_name="شروع (مثال: 1399)")
    end_year = models.CharField(max_length=20, verbose_name="پایان (یا اکنون)", blank=True)
    description = models.TextField(blank=True, verbose_name="توضیحات")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        ordering = ['order']
        verbose_name = "سوابق کاری"
        verbose_name_plural = "سوابق کاری"

    def __str__(self):
        return f"{self.job_title} - {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    tech = models.CharField(max_length=200, blank=True, verbose_name="تکنولوژی‌ها")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    link = models.URLField(blank=True, verbose_name="لینک (اختیاری)")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        ordering = ['order']
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=200, verbose_name="مدرک")
    university = models.CharField(max_length=200, verbose_name="موسسه/دانشگاه")
    duration = models.CharField(max_length=100, blank=True, verbose_name="بازه زمانی")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        ordering = ['order']
        verbose_name = "تحصیلات"
        verbose_name_plural = "تحصیلات"

    def __str__(self):
        return f"{self.degree} - {self.university}"
