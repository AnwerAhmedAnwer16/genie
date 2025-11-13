from modules.base.model_inheritance import ModelExtension
from .models.transport import Transport
from django.db import models 

class GuidExtension(ModelExtension):

    _inherit = 'base.partner'


    tours = models.TextField(blank=True, null=True)
    vichele = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=True)
    special_field = models.CharField(max_length=100, blank=True, null=True)
    # def __str__(self):
    #     return self.name