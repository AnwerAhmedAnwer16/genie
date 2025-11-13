from django.db import models
from .destination import *
from .tour import *
from modules.base.models import BaseModel


class Guide(BaseModel):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    tours = models.ManyToManyField(Tour, related_name='guides')

    def __str__(self):
        return self.name