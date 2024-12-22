from django.contrib import admin

from .models import CustomUser

from django.contrib import admin

admin.site.site_header = "AlgoVisualizer Admin Login"
admin.site.site_title = "AlgoVisualizer Administration Portal"
admin.site.index_title = "Welcome to AlgoVisualizer Admin Portal"


admin.site.register(CustomUser)

# Register your models here.