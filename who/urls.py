from django.contrib import admin
from django.urls import path,include,re_path
from .views import WHO,IndexList

urlpatterns = [
    path('',WHO.as_view()),
    path('index/',IndexList.as_view()),
]