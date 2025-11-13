from django.db import models
from .tour import Tour
from modules.base.models import BaseModel

class Destination(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/')
    created_at = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(Tour, on_delete = models.CASCADE, related_name='destinations')
    def __str__(self):
        return f"{self.name}, {self.city}"
