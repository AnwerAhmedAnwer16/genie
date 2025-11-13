from django.db import models
from .destination import *
from .tour import *
from modules.base.models.user import User
from modules.base.models import BaseModel


class TourBooking(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.user.username} - {self.tour.name} ({self.seats_booked} seats)"
