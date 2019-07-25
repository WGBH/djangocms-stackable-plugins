# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
from datetime import timedelta

from colorfield.fields import ColorField
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_link.validators import IntranetURLValidator
from filer.fields.image import FilerImageField

from .utils import _get_renderer_choices, _get_renderer_label
from .abstract_models import BaseAbstractPlugin, BaseObjectWithAttributes, BaseObjectWithStyleAttributes, BaseControlledVocabulary
from .helpers import format_hostedvideo_duration


GENERIC_ALIGNMENT_CHOICES = (
    ('left', 'Content Floats Left'),
    ('right', 'Content Floats Right'),
    ('center-block', 'Content breaks text, centered as its own block'),
    #('inline', 'Content are inline')
)


def get_upload_to(instance, filename):
    return instance.get_upload_to_path(filename)
    
######################################################################################################## 
######################################################################################################## GENERIC CONTAINER
######################################################################################################## 

class GenericContainerPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='GenericContainerPlugin'),
        null = True, blank = True
    )   
    
    alignment =  models.CharField (
        _('Content Alignment'),
        max_length = 40,
        choices = GENERIC_ALIGNMENT_CHOICES,
        null = True, blank = True,
        help_text = "Note: child plugins might also re-align their content"
    )
    
    #
    # Optional background image or color
    background_color = ColorField(null=True, blank=True)
    background_image = FilerImageField(null=True, blank=True, related_name='background_image', on_delete=models.CASCADE)
    
    def __str__(self):
        if self.title is None:
            return "- %d: (no Title) [%s]" % (self.pk, _get_renderer_label(self))
        else:
            return "- %d: %s [%s]" % (self.pk, self.title, _get_renderer_label(self))

######################################################################################################## 
######################################################################################################## GENERIC LIST
######################################################################################################## 

class GenericListPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='GenericListPlugin'),
        null = True, blank = True
    )    
    
    def __str__(self):
        if self.title is None:
            return "- %d: (no Title) [%s]" % (self.pk, _get_renderer_label(self))
        else:
            return "- %d: %s [%s]" % (self.pk, self.title, _get_renderer_label(self))
               
class GenericSeparatorPlugin(BaseAbstractPlugin, BaseObjectWithStyleAttributes):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='GenericSeparatorPlugin'),
        null = True, blank = True
    )
    separator_image = FilerImageField(
        null = True, blank = True,
        related_name = 'separator_image',
        help_text = 'If you want an image to be used, add it here (can be an icon or a banner)'
        on_delete = models.CASCADE
    )
    
    
TARGET_CHOICES = (
    ('_blank', _('Open in new window')),
    ('_self', _('Open in same window')),
)

HOSTNAME = getattr(
    settings,
    'DJANGOCMS_LINK_INTRANET_HOSTNAME_PATTERN',
    None
)

class GenericButtonPlugin(BaseAbstractPlugin, BaseObjectWithStyleAttributes):
    url_validators = [IntranetURLValidator(intranet_host_re=HOSTNAME),]
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='GenericButtonPlugin'),
        null = True, blank = True
    )
    external_link = models.URLField(
        verbose_name=_('External link'),
        blank=True,
        max_length=2040,
        validators=url_validators,
        help_text=_('Provide a valid URL to an external website.'),
    )
    internal_link = models.ForeignKey(
        Page,
        verbose_name=_('Internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )
    target = models.CharField(
        verbose_name=_('Target'),
        choices=TARGET_CHOICES,
        blank=True,
        max_length=255,
    )
    uploaded_file = models.FileField (
        verbose_name=_('File'),
        upload_to=('uploaded_files/'),
        blank = True,
        max_length = 255, 
        help_text = 'e.g., a PDF'
    )
    css_class = models.CharField (
        verbose_name=_('CSS Class'),
        blank = True, null=True,
        max_length = 255, 
        help_text = 'Apply your own custom CSS class to this button'
    )
    
    def get_link(self):
        if self.external_link:
            link = self.external_link
        elif self.internal_link_id:
            link = self.internal_link.get_absolute_url()
        elif self.uploaded_file:
            #print "FILE: ", self.uploaded_file
            #print "DIR: ", dir(self.uploaded_file)
            link = '/media/' + self.uploaded_file.name
        else:
            link = ''
        return link
        
        
######################################################################################################## 
######################################################################################################## RENDERED TEXT BLOCK
######################################################################################################## 



#IMAGE_ALIGNMENT_CHOICES = (
#    ('left', 'Images Float Left'),
#    ('right', 'Images Float Right'),
#    ('center-block', 'Images break text, centered as its own block'),
#    ('inline', 'Images are inline')
#)
#
#class RenderableTextPlugin(BaseAbstractPlugin):
#    renderer = models.CharField (
#        _('Renderer'),
#        max_length = 200,
#        choices = _get_renderer_choices(parent_model='RenderableTextPlugin'),
#        default = _get_renderer_choices(parent_model='RenderableTextPlugin')[0][0],
#        null = True, blank = True
#    )
#    text_block = HTMLField(configuration='CKEDITOR_HTMLFIELD_SETTINGS')
#    image_alignment = models.CharField (
#        _('Image Alignment'),
#        max_length = 40,
#        choices = IMAGE_ALIGNMENT_CHOICES,
#        null = False, default = None
#    )
#
#    def __str__(self):
#        if self.title is None:
#            return " - %d: %s [%s]" % (self.pk, self.text_block[:50], _get_renderer_label(self))
#        else:
#            return " - %d: %s [%s]" % (self.pk, self.title, _get_renderer_label(self))
 
 

######################################################################################################## 
######################################################################################################## CUSTOM PLUGINS
######################################################################################################## 
class ImageWithThumbnailPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model = 'ImageWithThumbnailPlugin'),
        default = _get_renderer_choices(parent_model = 'ImageWithThumbnailPlugin')[0][0],
        null = True, blank = True
    )
    main_image = models.ImageField (
        _('Primary Image'),
        upload_to = get_upload_to,
        null = True, blank = True,
        width_field='main_image_width', height_field='main_image_height', #ppoi_field='main_image_ppoi',
        help_text = 'Upload full-sized image.'
    )
    main_image_height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    main_image_width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    thumbnail = models.ImageField (
        _('Thumbnail Image'),
        upload_to = get_upload_to,
        null = True, blank = True,
        width_field='thumbnail_width', height_field='thumbnail_height', 
    )
    thumbnail_height = models.PositiveIntegerField(
        'Thumbnail Height',
        blank=True,
        null=True,
        default = 64
    )
    thumbnail_width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True,
        default = 64
    )
    caption = HTMLField()
    credit = models.CharField(
        _('Image Credit'),
        max_length = 255,
        null = True, blank = True
    )
    
    def get_upload_to_path(instance, filename):
        return 'gallery_images/'+filename
    
    def __str__(self):
        return self.title
        
    
######################################################################################################## 
######################################################################################################## HOSTED VIDEO
########################################################################################################
class HostService(BaseControlledVocabulary):
    pass
    
    class Meta:
        verbose_name = 'Video Hosting Service'
        verbose_name_plural = 'Video Hosting Services'
    
    def __str__(self):
        return self.title
        
class HostedVideoPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='HostedVideoPlugin'),
        default = _get_renderer_choices(parent_model='HostedVideoPlugin')[0][0],
        null = True, blank = True
    )
    host = models.ForeignKey(HostService, null=False, on_delete=models.CASCADE)
    id_on_service = models.CharField (
        _('ID on Service'),
        max_length = 200,
        null = False,
        help_text = 'For PBS COVE, enter the COVE ID here.'
    )
    duration = models.DurationField (
        _('Duration'),
        null = True, blank = True, default = timedelta(),
        help_text = '[DD] [HH:[MM:]]ss[.uuuuuu]'
    )
    title = models.CharField (
        _('Title'),
        max_length = 200,
        null = True, blank = True
    )
    #description = HTMLField(configuration='CKEDITOR_HTMLFIELD_SETTINGS', null=True, blank=True)
    description = models.TextField (
        _('Video Caption'),
        null = True, blank = True
    )
    
    def __format_duration(self):
        return format_hostedvideo_duration(self.duration)
    format_duration = property(__format_duration)
    
    def __str__(self):
        return "%s: %s" % (self.host.title, self.id_on_service)
    
######################################################################################################## 
######################################################################################################## CUSTOM PLUGINS
######################################################################################################## 

class BiographyPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='BiographyPlugin'),
        default = _get_renderer_choices(parent_model='BiographyPlugin')[0][0],
        null = True, blank = True
    )
    headshot = FilerImageField ( 
        null = True,
        blank = True,
    )
    name = models.CharField (
        _('Name'),
        max_length = 200,
        null = False
    )
    byline = models.CharField (
        _('Byline'),
        max_length = 200,
        null = True,
        blank = True
    )
    text_block = HTMLField(configuration='CKEDITOR_HTMLFIELD_SETTINGS')
    
class CountdownClockPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='CountdownClockPlugin'),
        default = _get_renderer_choices(parent_model='CountdownClockPlugin')[0][0],
        null = True, blank = True
    )
    
    zero_date_time = models.DateTimeField (
        _('Zero'),
        null = False
    )
    
    label = models.CharField (
        _('Label'),
        max_length = 400,
        null = True, blank = True,
        help_text = "This is a label that appears with the clock, e.g., \'Series Premiere in...\'"
    )
    

CONJUNCTION_CHOICES = ( ('and', 'And'), ('or', 'Or'), ('versus', 'Vs.') )
class CompareTwoThingsPlugin(BaseAbstractPlugin):
    renderer = models.CharField (
        _('Renderer'),
        max_length = 200,
        choices = _get_renderer_choices(parent_model='CompareTwoThingsPlugin'),
        default = _get_renderer_choices(parent_model='CompareTwoThingsPlugin')[0][0],
        null = True, blank = True
    )
    
    title_left = models.CharField (
        _('Left Title'),
        max_length = 200,
        null = False,
    )
    image_left = FilerImageField(
        null = False, related_name = 'left_image'
    )
    body_left = HTMLField(configuration='CKEDITOR_HTMLFIELD_SETTINGS')

    conjunction = models.CharField(
        _('Comparison Conjuction'),
        null = True, blank = True,
        choices = CONJUNCTION_CHOICES,
        max_length = 10
    )

    title_right = models.CharField (
        _('Right Title'),
        max_length = 200,
        null = False
    )
    image_right = FilerImageField(
        null = False, related_name = 'right_image'
    )
    body_right = HTMLField(configuration='CKEDITOR_HTMLFIELD_SETTINGS')


    def __str__(self):
        return " - %d: %s %s %s [%s]" % (self.pk, self.title_left, self.conjunction, self.title_right, _get_renderer_label(self))

