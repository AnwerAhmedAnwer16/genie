from django.contrib import admin

# Register your models here.
from .models.destination import Destination
from .models.tour import Tour
from .models.category import Category
from .models.guide import Guide
from .models.review import Review
from .models.tour_booking import TourBooking
from .models.transport import Transport

admin.site.register(Transport)
admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Guide)
admin.site.register(Review)
admin.site.register(TourBooking) 