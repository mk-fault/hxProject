from django.contrib import admin
from django.urls import path,include,re_path
from .views import OECD,IndexList

urlpatterns = [
    path('',OECD.as_view()),
    path('index/',IndexList.as_view()),
]