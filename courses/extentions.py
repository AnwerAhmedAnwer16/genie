from modules.base.model_inheritance import ModelExtension
from modules.crm.models import * 
from django.db import models


class CoursesExtension(ModelExtension):

    _inherit = 'base.partner'
    is_instructor = models.BooleanField(default=False)
    
class CrmCourseExtension(ModelExtension):
    _inherit = 'crm.lead'

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='leads' )