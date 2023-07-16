from django.contrib import admin
from django.urls import path,include,re_path
from .views import QG

urlpatterns = [
    path('qg/',QG.as_view()),
]