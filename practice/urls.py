"""
URL configuration for practice project.

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
from django.urls import path, include

from skolkovo.views import index, grants, services, quick_logout, navigator, my_companies, create_company, \
    create_product, delete_company, delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('grants/', grants, name='grants'),
    path('services/', services, name='services'),
    path('navigator/', navigator, name='navigator'),
    path('navigator/my_companies/', my_companies, name='my_companies'),
    path('navigator/my_companies/create', create_company),
    path('navigator/my_companies/<int:company_id>/create_product', create_product),
    path('navigator/my_companies/<int:company_id>/delete', delete_company),
    path('navigator/my_companies/delete_product/<int:product_id>', delete_product),

    path('accounts/', include('allauth.urls')),
    path('logout/', quick_logout, name='logout'),
]
