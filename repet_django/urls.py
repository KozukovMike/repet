"""
URL configuration for repet_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from base import views as base_views
from about import views as about_views
from check import views as check_views


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', base_views.custom_logout, name='logout'),
    path('task_page/', check_views.task_page, name='task_page'),
    path('task_page/class/5', check_views.class5_page, name='class5'),
    path('task_page/class/6', check_views.class6_page, name='class6'),
    path('task_page/class/7', check_views.class7_page, name='class7'),
    path('task_page/class/8', check_views.class8_page, name='class8'),
    path('task_page/class/9', check_views.class9_page, name='class9'),
    path('task_page/class/10', check_views.class10_page, name='class10'),
    path('task_page/class/11', check_views.class11_page, name='class11'),
    path('test/<int:test_id>/', check_views.test_view, name='test'),
    path('register/', user_views.register, name='register'),
    path('home/', base_views.home, name='home'),
    path('about/', about_views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
