from home import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('about', views.about, name = 'about')
]

