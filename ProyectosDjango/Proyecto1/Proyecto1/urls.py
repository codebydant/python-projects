"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Proyecto1.views import saludo, despedida, get_date, calculate_futAge, get_template, get_template_loader, get_template_shorcuts
from Proyecto1.views import get_template_padre, get_template_child

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('date/', get_date),
    path('futage/<int:age_>/<int:year_>', calculate_futAge),
    path('template/', get_template),
    path('loader/', get_template_loader),
    path('render/', get_template_shorcuts),
    path('inheritance-padre/', get_template_padre),
    path('inheritance-child/', get_template_child)

]
