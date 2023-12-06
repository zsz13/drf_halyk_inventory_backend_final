"""
URL configuration for drfhalyksite project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.backends import django
from django.urls import re_path as url
from django.templatetags.static import static as django_static
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from drfhalyksite import settings
from inventory.views import InventoryItemAPIList, InventoryItemAPIUpdate, InventoryItemAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/inventory-auth/', include('rest_framework.urls')),
    path('api/v1/inventoryitem/', InventoryItemAPIList.as_view()),
    path('api/v1/inventoryitem/<int:pk>/', InventoryItemAPIUpdate.as_view()),
    path('api/v1/inventoryitemdelete/<int:pk>/', InventoryItemAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/inventory/images/favicon.ico')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
