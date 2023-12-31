"""
URL configuration for hxProject project.

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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/stats/',include('stats.urls')),
    path('api/wb/',include('wb.urls')),
    path('api/who/',include('who.urls')),
    path('api/oecd/',include('oecd.urls')),
    path('api/gbd/',include('gbd.urls')),
    path('api/docs/',include_docs_urls(title='录取通知书API文档')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
