from django.utils.translation import gettext as _
courses_partner_forn_views_patch ={
    "key" : "courses_partner_forn_views_patch",
    "name": "Courses Partner Form Views Patch",
    "model" : 'base.partner',
    "view_type" : 'form',
    "inherit_mode" : "extension",
    "inherit_id" : "base_partner_form_view",
    "module" : "contacts",
    "inheritance_operations":
        [{
        "operation":"append",
        "target" : "sheet.title.fields",
        "content":[
            {
                'name': 'is_teacher',
                'widget': 'switch',
                'string': _('Is Instructor'),
            }
        ]
    }]
}

courses_crm_lead_form_view_patch = {
    "key" : "courses_crm_lead_form_view_patch",
    "name": "Courses CRMLead Form View Patch",
    "model" : 'crm.lead',
    "view_type" : 'form',
    "inherit_mode" : "extension",
    "inherit_id" : "crm_lead_form_view",
    "module" : "crm",
    "inheritance_operations":
        [{
        "operation":"append",
        "target" : "sheet.groups.0.groups.0.fields",
        "content":{
                'name': 'course',
                'widget': 'relation',
                'string': _('Course'),
            }
    }]
}


