from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# Models for courses module
from modules.base.models.base import BaseModel 

class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name
    

class Level(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null= True)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    

class Package(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Courses(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name= "courses")
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name= "courses")
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_published = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default= 2.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name