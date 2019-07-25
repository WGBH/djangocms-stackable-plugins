class CustomCMSPluginMixin(object):
    pass

    def get_render_template(self, context, instance, placeholder):
        if instance.renderer:
            return instance.renderer
        return self.render_template # default
