from home import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('logout', views.logoutuser, name = 'logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path("profile/", views.profile_view, name="profile"),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('about/', views.about, name='about'),
    path('ssort/',views.selection_sort,name= 'selection_sort'),
    path('bsort/',views.bubble_sort,name= 'bubble_sort'),
    path('inssort/',views.insertion_sort,name= 'insertion_sort'),
    path('insdel/',views.insdel,name= 'insdel'),
    path('stack_visualizer/',views.stack_visualizer,name= 'stack_visualizer'),
    path('queue_visualizer/',views.queue_visualizer,name= 'queue_visualizer'),
    path('set_language/', views.set_language, name='set_language'),
    
]
