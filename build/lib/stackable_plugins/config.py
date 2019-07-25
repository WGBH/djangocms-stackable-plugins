#  Each key is the name of a CMSPlugin model, values are tuples with the following fields:
#   0 - slug (not stored in database, helpful for categorizing)
#   1 - short description
#   2 = template (this is what is stored in the database)
#   3 - long description - used for help_text
#
# The FIRST item in the list is the default
DEFAULT_PLUGIN_RENDERER_TEMPLATES = {
    'GenericButtonPlugin':
        [
            (   'generic_container',
                'DEFAULT: Generic Button - a container for children plugins',
                'renderers_by_class/rendered_button/default.html',
                'Used to create a generic button'
            ),
        ],
    'GenericContainerPlugin':
        [
            (   'generic_container',
                'DEFAULT: Generic Parent - a container for children plugins',
                'renderers_by_class/rendered_generic/default_generic_container.html',
                'Used to define a block of plugins'
            ),
            (   'accordion_container',
                'Accordion: Used to hide/show plugin content on click', 
                'renderers_by_class/rendered_generic/accordion_container.html',
                'Used to define a block of plugins'
            ),
        ],
    'GenericListPlugin':
        [
            (   '1_up',
                'DEFAULT: one item per row',
                'renderers_by_class/rendered_list/default.html',
                'Show each item within a single-column list of blocks',
            ),
            (   '2_up',
                'Two items per row',
                'renderers_by_class/rendered_list/2_up.html',
                'Show two items per row (ordering is across then down)'
            ),
            (   '3_up',
                'Three items per row',
                'renderers_by_class/rendered_list/3_up.html',
                'Show three items per row (ordering is across then down)'
            ),
            (   'bulleted_list',
                'Bulleted list of items (links only)',
                'renderers_by_class/rendered_list/bulleted_list.html',
                'Create a bulleted list of items (each line links to an item)'
            ),
            (   'carousel',
                'Items displayed in a carousel',
                'renderers_by_class/rendered_list/carousel.html',
                'Canonical image of each item appears in a carousel',
            ),
        ],
    'GenericSeparatorPlugin':
        [
            (   'horizontal_rule',
                'DEFAULT: Generic Separator - a horizontal rule',
                'renderers_by_class/rendered_separator/default_generic_separator.html',
                'Simple horizontal rule.'
            ),
            (   'center_icon',
                'A centered image - can be icon or a banner',
                'renderers_by_class/rendered_separator/image_separator.html',
                'Separation using an image - either an icon or a banner-like image.'
            ),
        ],
    'ImageWithThumbnailPlugin':
        [
            (   'default',
                'DEFAULT: Thumbnail clickable to show main image',
                'renderers_by_class/rendered_image/default.html',
                'Shows the Thumbnail which is clickable to show the main image',
            ),
        ],
    'HostedVideoPlugin':
        [
            (   'default',
                'DEFAULT: COVE video',
                'renderers_by_class/hosted_video/default.html',
                'Renders a COVE video given the COVE ID.'
            ),
        ],
    'BiographyPlugin':
        [
            (   'default',
                'DEFAULT: Biography',
                'renderers_by_class/rendered_biography/default.html',
                'Creates a bio with: name, byline, headshot, and text.'
            ),
        ],
    'CountdownClockPlugin':
        [
            (   'default',
                'DEFAULT: Countdown Clock',
                'renderers_by_class/rendered_countdown/default.html',
                'Creates a simple countdown clock.'
            ),
        ],
    'CompareTwoThingsPlugin':
        [
            (   'default',
                'DEFAULT: Side by Side Comparison - Image above Text block',
                'renderers_by_class/rendered_comparison/default.html',
                'Creates two side-by-side blocks, each with an image over text.  Optional middle "conjunction" (for things like "vs.", "and", "or")'
            ),
        ],
}

#    'RenderableTextPlugin':
#        (
#            (   'full_width',
#                'DEFAULT: full width',
#                'renderers_by_class/rendered_text/default.html',
#                'Text rendered using the full width of the parent container (div).'
#            ),
#            (   'text_left_ad_right',
#                'Text on Left, Ad on Right',
#                'renderers_by_class/rendered_text/text_left_ad_right.html',
#                'Text rendered on Left, Ad on right'
#            ),
#        ),