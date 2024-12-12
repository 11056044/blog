"""
URL configuration for mblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from mysite.views import *
from mblog import *

urlpatterns = [
    path("admin/", admin.site.urls), # 管理后台
    path('',homepage), # 首页
    path('post/', homepage),  # 如果你想在 /post/ 显示所有帖子
    path('post/<slug:slug>/', showpost),  # 单个帖子的详细页面
   
    
]
