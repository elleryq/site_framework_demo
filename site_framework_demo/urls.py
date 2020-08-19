"""site_framework_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.SITE_ID == 0:
    urlpatterns += [
        path('blog/', include('blog.urls')),
        path('news/', include('news.urls')),
    ]
elif settings.SITE_ID == 1:
    urlpatterns += [
        path('blog/', include('blog.urls')),
    ]
elif settings.SITE_ID == 2:
    urlpatterns += [
        path('news/', include('news.urls')),
    ]
