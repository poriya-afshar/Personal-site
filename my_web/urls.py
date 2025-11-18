from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import views, settings

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('single-blog/', views.single_blog, name='single-blog'),
    path('resume/', views.resume, name='resume'),
    path('blog/', include('blog.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
