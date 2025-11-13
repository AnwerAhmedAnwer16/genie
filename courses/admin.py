from django.contrib import admin
from .models import Category, Level, Package, Courses
# Register your models here.
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Package)
admin.site.register(Courses)
