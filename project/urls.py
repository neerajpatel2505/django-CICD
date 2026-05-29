"""
URL configuration for project project.

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
print("From urls.py....................")

from django.contrib import admin
from django.urls import path
# from app1 import views

# from app1.views import home,home1,landing 
from app1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home, name='home') # recommended from app1 import views
    path('home/', home, name='home'), # recommended from app1.views import home
    path("home1/",home1,name="home1"),
    path('',landing,name="landing")
]
