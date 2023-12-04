"""
URL configuration for components1 project.

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
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('badge/',badge,name='badge'),
    path('breadcrumb/',breadcrumb,name='breadcrumb'),
    path('buttons/',buttons,name='buttons'),
    path('button_groups/',button_groups,name='button_groups'),
    path('collapse/',collapse,name='collapse'),
    path('droupdowns/',droupdowns,name='droupdowns'),
    path('forms/',forms,name='forms'),
    path('input_groups/',input_groups,name='input_groups'),
    path('jumbotron/',jumbotron,name='jumbotron'),
    path('list_group/',list_group,name='list_group'),
    path('media_object/',media_object,name='media_object'),
]
