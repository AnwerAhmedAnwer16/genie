from django.db import models
from .destination import *
from .tour import *
from modules.base.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tours = models.ManyToManyField(Tour, related_name='categories', blank=True)

    def __str__(self):
        return self.name