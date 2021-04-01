from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()