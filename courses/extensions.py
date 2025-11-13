from modules.base.model_inheritance import ModelExtension
from courses.models import Courses
from modules.base.decorators import action
from django.db import models

class PartnerExtensioncourse(ModelExtension):
    _inherit = 'base.partner'
    
    
    is_teacher = models.BooleanField(default=False,blank=True,null=True)
    
class CrmCourseExtension(ModelExtension):
    _inherit = 'crm.lead'

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='leads', blank=True, null=True)


class CoureseInChat(ModelExtension):
    _inherit = 'chat.conversation'

    @action
    def get_courses(self):
        return {
                'status' : True,
                'open_mode' : 'slideover',
                'data' : {
                    'menu_item_key' : 'courses_gchild_menu_courses',
                    'view_type' : 'list'
                },
                'title': 'courses'

        }
    
