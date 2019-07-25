from django.contrib import admin
from .models import GenericContainerPlugin, CompareTwoThingsPlugin, GenericListPlugin, ImageWithThumbnailPlugin, HostService
#from .models import RenderableTextPlugin, GenericContainerPlugin, CompareTwoThingsPlugin, GenericListPlugin, ImageWithThumbnailPlugin, HostService

admin.site.register(HostService)

#admin.site.register(ImageWithThumbnailPlugin)
#admin.site.register(RenderableTextPlugin)
#admin.site.register(CompareTwoThingsPlugin)
#admin.site.register(GenericContainerPlugin)
#admin.site.register(GenericListPlugin)