from django.conf import settings
from .config import DEFAULT_PLUGIN_RENDERER_TEMPLATES

######################################################################################################## 
######################################################################################################## MODEL FUNCTIONS
######################################################################################################## 

def _get_renderer_choices(parent_model=None):
    if parent_model is None:
        return None # will go to the default
    
    default_choices = additional_choices = []
    all_additional_choices = getattr(settings, 'ADDITIONAL_PLUGIN_RENDERER_TEMPLATES', None)
    
    if parent_model in DEFAULT_PLUGIN_RENDERER_TEMPLATES.keys():
        default_choices = DEFAULT_PLUGIN_RENDERER_TEMPLATES[parent_model]
    if all_additional_choices and parent_model in all_additional_choices.keys():
        additional_choices = all_additional_choices[parent_model]
        
    renderer_choices = default_choices + additional_choices
    template_choices = list()
    for r in renderer_choices:
        this_r = (r[2], r[1])
        template_choices.append(this_r)
    return template_choices
    
def _get_renderer_label(obj):
    if obj.renderer is None:
        return 'default'
    else:
        return obj.get_renderer_display()
