from django.contrib import admin
from .models import * # (*) import all models 

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)