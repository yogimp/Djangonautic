from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('about/', views.article_list),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),
]
