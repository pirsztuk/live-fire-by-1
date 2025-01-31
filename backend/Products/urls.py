"""
URL configuration for LiveFire project.

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
from django.urls import path

from . import views

urlpatterns = [
    path('get_products/', views.ProductsView.as_view(), name='get_products'),
    
    path('create_product/', views.ProductView.as_view(), name='create_product'),
    path('get_product/', views.ProductView.as_view(), name='get_product'),
    path('update_product/', views.ProductView.as_view(), name='update_product'),
    path('delete_product/', views.ProductView.as_view(), name='delete_product'),
]
