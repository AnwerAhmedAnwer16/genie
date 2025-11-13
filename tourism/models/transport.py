from django.db import models
from .destination import *
from .tour import *
from modules.base.models import BaseModel

class Transport(BaseModel):
    TOUR_TRANSPORT_CHOICES = [
        ('bus', 'Bus'),
        ('van', 'Van'),
        ('car', 'Car'),
        ('bike', 'Bike'),
    ]
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='transports')
    type = models.CharField(max_length=20, choices=TOUR_TRANSPORT_CHOICES)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type.capitalize()} for {self.tour.name}"
