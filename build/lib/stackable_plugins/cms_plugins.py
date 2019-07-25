from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .mixins import CustomCMSPluginMixin

import datetime, pytz
from django.conf import settings
from django.utils.translation import ugettext as _

from .models import GenericContainerPlugin, GenericListPlugin, GenericSeparatorPlugin, GenericButtonPlugin
from .models import CountdownClockPlugin,  CompareTwoThingsPlugin, ImageWithThumbnailPlugin, HostedVideoPlugin
from .models import BiographyPlugin #, RenderableTextPlugin,


################################################################################ GENERIC PLUGINS
class CMSGenericContainerPlugin(CMSPluginBase,CustomCMSPluginMixin):
    model = GenericContainerPlugin
    name = _('Generic Container Plugin')
    render_template = 'renderers_by_class/rendered_generic/default_generic_container.html'
    allow_children = True
    module = 'Stackable Plugins'
    
    fieldsets = (
        (None, 
            {
                'fields': ( 'renderer', 'title' ),
            },
        ),
        ('Background Options',
            {
                'fields': (
                    'background_color',
                    'background_image',
                ),
                'classes': ( 'collapse', ),
            },
        ),
        #('Styling Options', { 'fields': ( 'main_image', 'thumbnail' ), }, ),
    )
    
    def render(self, context, instance, placeholder):
        context = super(CMSGenericContainerPlugin, self).render(context, instance, placeholder)
        return context
        
class CMSGenericListPlugin(CMSPluginBase):
    model = GenericListPlugin
    name = _('Generic List/Gallery Plugin')
    render_template = 'renderers_by_class/rendered_list/default.html'
    allow_children = True
    module = 'Stackable Plugins'
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
    
    def render(self, context, instance, placeholder):
        context = super(CMSGenericListPlugin, self).render(context, instance, placeholder)
        #
        # I suspect that this will be more involved than the other plugins because the nature of the renderers will likely
        #   require different setups.
        #
        # One thing to consider: should we use the instance.renderer value in a control block, or should we create "everything"
        #   we'd need and send it along blindly...?
        #
        return context
        
class CMSGenericButtonPlugin(CMSPluginBase):
    model = GenericButtonPlugin
    name = _('Generic Button Plugin')
    render_template = 'renderers_by_class/rendered_button/default.html'    
    module = 'Stackable Plugins'
    
    fieldsets = (
        (None, { 'fields': ( 'title', 'renderer', 'css_class', ),  }, ),
        ('Links:', { 'fields': (('external_link', 'internal_link'), 'uploaded_file', 'target', ),}, ),
        ('Attributes (optional)', { 'classes': ('collapse', ), 'fields': ('style_attributes', ), }, ),
    )

    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
    
    def render(self, context, instance, placeholder):
        context = super(CMSGenericButtonPlugin, self).render(context, instance, placeholder)
        return context
        
class CMSGenericSeparatorPlugin(CMSPluginBase):
    model = GenericSeparatorPlugin
    name = _('Generic Separator Plugin')
    render_template = 'renderers_by_class/generic_separator/default.html'
    module = 'Stackable Plugins'
    
    fieldsets = (
        (None, { 'fields': ( 'title', 'renderer', ), }, ),
        ('Image (optional)', { 'classes': ('collapse', ), 'fields': ('separator_image', ), }, ),
        ('Attributes (optional)', { 'classes': ('collapse', ), 'fields': ('style_attributes', ), }, ),
    )
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
    
    def render(self, context, instance, placeholder):
        context = super(CMSGenericSeparatorPlugin, self).render(context, instance, placeholder)
        return context
        
################################################################################ CUSTOM PLUGINS
#class CMSRenderableTextPlugin(CMSPluginBase):
#    model = RenderableTextPlugin
#    name = _('Renderable Text Plugin')
#    render_template = 'renderers_by_class/rendered_text/default.html'
#    module = 'Stackable Plugins'
#
#    def get_render_template(self, context, instance, placeholder):
#        if instance.renderer:
#            #print "RENDERER: ", instance.renderer
#            return instance.renderer
#        return self.render_template # default
#
#    def render(self, context, instance, placeholder):
#        context = super(CMSRenderableTextPlugin, self).render(context, instance, placeholder)
#        context['body'] = instance.text_block
#        context['image_alignment'] = instance.image_alignment
#        return context

class CMSImageWithThumbnailPlugin(CMSPluginBase):
    model = ImageWithThumbnailPlugin
    name = _('Image With Thumbnail Plugin')
    render_template = 'renderers_by_class/rendered_image/default.html'
    module = 'Stackable Plugins'
    
    exclude = ('main_image_width', 'main_image_height', 'main_image_ppoi', 'thumbnail_width', 'thumbnail_height', 'thumbnail_ppoi')
    fieldsets = (
        (None, { 'fields': ( 'renderer', ), }, ),
        ('Text', { 'fields': ( 'title', 'caption', 'credit' ), }, ),
        ('Images', { 'fields': ( 'main_image', 'thumbnail' ), }, ),
    )
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
        
    def render(self, context, instance, placeholder):
        context = super(CMSImageWithThumbnailPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context

class CMSHostedVideoPlugin(CMSPluginBase):
    model = HostedVideoPlugin
    name = _('Hosted Video Plugin')
    render_template = 'renderers_by_class/hosted_video/default.html'
    module = 'Stackable Plugins'
    
    fieldsets = (
        (None, { 'fields': (
                    'renderer', 
                    ('host', 'id_on_service', ),
                    'duration',
                    'title',
                    'description',
                ), }, ),
        )
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
        
    def render(self, context, instance, placeholder):
        context = super(CMSHostedVideoPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context

class CMSCountdownClockPlugin(CMSPluginBase):
    model = CountdownClockPlugin
    name = _('Countdown Clock Plugin')
    render_template = 'renderers_by_class/rendered_countdown/default.html'
    module = 'Stackable Plugins'
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
        
    def render(self, context, instance, placeholder):
        """ 
        OK:  so we have to be cognisant of time zones here.
            In the admin, the zero_date_time is entered in LOCALLY
            BUT it is stored in the DB in UTC.
            
            using tzlocal() gets the local time.
            BECAUSE it is "time zone aware" it's OK to do the simple subtraction to get the 
            time to the countdown.
        """
        context = super(CMSCountdownClockPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
    
        now = datetime.datetime.now(pytz.timezone(getattr(settings, 'TIMEZONE', 'UTC')))
        context['now'] = now
        t_minus = instance.zero_date_time - now
        context['t_minus'] = t_minus
        context['total_seconds'] = t_minus.total_seconds()
        context['in_the_past'] = (t_minus.total_seconds() < 0)
        
        context['t_minus_days'] = t_minus.days
        context['t_minus_hours'] = t_minus.seconds // 3600
        context['t_minus_minutes'] = (t_minus.seconds % 3600) // 60
        context['t_minus_seconds'] = t_minus.seconds % 60
        context['unixtime'] = instance.zero_date_time.strftime("%s")
        context['unixtime_now'] = now.strftime("%s")
        context['delta_seconds'] = t_minus.total_seconds()
        
        return context
        
class CMSBiographyPlugin(CMSPluginBase):
    model = BiographyPlugin
    name = _('Biography Plugin')
    render_template = 'renderers_by_class/rendered_biography/default.html'
    module = 'Stackable Plugins'
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
    
    def render(self, context, instance, placeholder):
        context = super(CMSBiographyPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context

class CMSCompareTwoThingsPlugin(CMSPluginBase):
    model = CompareTwoThingsPlugin
    name = _('Side by Side Comparison Plugin')
    render_template = 'renderers_by_class/rendered_comparison/default.html'
    module = _('Stackable Custom Plugins')
    
    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
        
    def render(self, context, instance, placeholder):
        context = super(CMSCompareTwoThingsPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context
        
plugin_pool.register_plugin(CMSGenericContainerPlugin)
plugin_pool.register_plugin(CMSGenericButtonPlugin)
plugin_pool.register_plugin(CMSGenericListPlugin)
plugin_pool.register_plugin(CMSGenericSeparatorPlugin)
#plugin_pool.register_plugin(CMSRenderableTextPlugin)
plugin_pool.register_plugin(CMSHostedVideoPlugin)
plugin_pool.register_plugin(CMSBiographyPlugin)
plugin_pool.register_plugin(CMSImageWithThumbnailPlugin)
plugin_pool.register_plugin(CMSCountdownClockPlugin)
plugin_pool.register_plugin(CMSCompareTwoThingsPlugin)