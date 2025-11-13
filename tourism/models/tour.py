from django.db import models
from numpy import record
from modules.base.models import BaseModel
from modules.base.decorators import onchange
from modules.base.decorators import action

class Tour(BaseModel):
    # destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tours')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()
    available_seats = models.PositiveIntegerField()
    start_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} - {self.destination.name}"

    @onchange('price')
    def _update_price_discount(self):
        if self.price:
            self.name = "shehab ..."  

    @action
    def discount_by100(queryset):
        for record in queryset:
                record.name = '888'
                record.save()
        return{
            'status': True,
            'open_mode' : 'message',
            'message' : f'Discount applied by 200%',
            'data' : {

            }
        }