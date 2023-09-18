from django.contrib import admin
from django.urls import path,include,re_path
from .views import QG, GS

urlpatterns = [
    path('qg/',QG.as_view()),
    path('gs/',GS.as_view()),
]