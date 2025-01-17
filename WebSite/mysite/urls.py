"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.static import serve

def handler404(request, exception):
    if request.user.is_authenticated:
        print('True')
        return render(request, '404.html')
    else:
        print('Fail')
        return render(request, '1404.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('password/reset/', auth_views.LoginView.as_view(template_name='login.html'), name='logout'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = handler404
