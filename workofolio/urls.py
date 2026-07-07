"""
URL configuration for workofolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('aboutme.urls'), name='aboutme'),
    path('', include('home.urls'), name='home'),
    path('education/', include('education.urls'), name='education'),
    path('projects/', include('projects.urls'), name='projects'),
    path('experience/', include('experience.urls'), name='experience'),
    path('skills/', include('skills.urls'), name='skills'),
    path('contact/', include('contact.urls'), name='contact'),
]
