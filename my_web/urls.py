from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views,settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('single-blog/', views.single_blog, name='single-blog')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)