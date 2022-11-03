"""QC_CUTS URL Configuration

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
from CUTS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_supplier, name='get_supplier'),
    path('add_supplier', views.add_supplier, name='add_supplier'),
    path('edit_supplier/<supplier_id>', views.edit_supplier, name='edit_supplier'),
    path('delete_supplier/<supplier_id>', views.delete_supplier, name='delete_supplier'),
    path('get_ranges/<supplier_id>', views.get_ranges, name='get_ranges'),
    path('add_range', views.add_range, name='add_range'),
    path('edit_range/<range_id>', views.edit_range, name='edit_range'),
    path('delete_range/<range_id>', views.delete_range, name='delete_range'),
]
