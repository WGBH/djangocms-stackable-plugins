from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
#from djangocms_text_ckeditor.fields import HTMLField
from djangocms_attributes_field.fields import AttributesField

###################################################################################################
################################################################################################### ABSTRACT ATTRIBUTES CLASSES
###################################################################################################    
class BaseAbstractPlugin(CMSPlugin):
    title = models.CharField (
        _('Title'),
        max_length = 200,
        null = True, blank = True
    )
    # This can't have renderer because that needs to know the class name...

    class Meta:
        abstract = True

class BaseObjectWithAttributes(models.Model):   
    attributes = AttributesField(
        _('Attributes'),
        blank=True,
        excluded_keys=['href', 'target'],
    )
    
    class Meta:
        abstract = True
        
class BaseObjectWithStyleAttributes(models.Model):
    style_attributes = AttributesField (
        _('Style Attributes'),
        blank = True,
    )
    
    class Meta:
        abstract = True
    
    def __attributes_as_style(self):
        entries = []
        if len(self.style_attributes) < 1:
            return ""
        keys = self.style_attributes.keys()
        
        for key in keys:
            this_style = "%s: %s" % (key, self.style_attributes[key])
            entries.append(this_style)
        return '; '.join(entries)
    attributes_as_style = property(__attributes_as_style)
    
class BaseControlledVocabulary(models.Model):
    title = models.CharField (
        _('Title'),
        max_length = 200,
        null = False
    )
    slug = models.SlugField (
        unique = True,
        null = False,
        max_length = 120,
    )
    available = models.BooleanField (
        _('Available'),
        null = False,
        default = True,
    )
    date_created = models.DateTimeField (
        _('Date Created'),
        auto_now_add = True
    )
    date_modified = models.DateTimeField (
        _('Last Updated'),
        auto_now = True
    )
    
    class Meta:
        abstract = True