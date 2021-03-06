# 1.0. Stackable Plugins

Stackable Plugins are a set of Django CMS plugins to make it easy for content managers to build somewhat custom pages.

They fall into two broad categories:

1. Page Framework plugins - where you can create grids of content;
2. Custom Function plugins - these are a loose library of plugins that were created for past projects.

## 1.1. Features

1. Each plugin has one or more renderers.  This allows the content to be rendered/displayed in different ways.  For example a generic list that contains callouts with an image, title, and short description, can be rendered as a list, in a grid, in a slideshow, or in a carousel (or in any other way your designer might dream up!), but the *content* is the same.   You can switch between renderers on the fly!

2. You can add renderers to any plugin.

3. Some plugins (like the Generic Container) can have children plugins.   


## 1.2. Quick start

1. Install and set up Django CMS

2. Add "stackable_plugins" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...
        'stackable_plugins',
    ]
    ```
    
3. Run `manage.py migrate stackable_plugins`

# 2.0 The Plugins

## 2.1. Page Framework Plugins

These allow you to "frame out" the content within a page's placeholder.

### 2.1.1. GenericContainerPlugin

Fundamentally, this is just a box of other plugins.  It's a way to segregate content on the page when you need that content treated as a group.

### 2.1.2. GenericListPlugin

This is a wrapper for a list of curated content.   The items in the List do NOT have to be of the same type:  you can create a list with an Image, a Video, then a blob of text, then another Video, then a List within the List, etc.

### 2.1.3. GenericSeparatorPlugin

This is a way to make fancy content separators (the most generic of which is the `<hr>` tag).

Typically this is used with a separator image.

### 2.1.4. GenericButtonPlugin

Why have a link when you can have a button?

These are very customizable!  

* Links can be External or Internal OR to a File (e.g., a PDF File);
* The link target can be to a new window, etc.;
* You can use any custom CSS class to render the generic button;
* You can set attibutes on the button (colors, etc.)

## 2.2. Content Plugins

These plugins have more structured content but have somewhat generic functions: e.g., a video player that can be used for YouTube, PBSMM, Vimeo, etc.

### 2.2.1. ImageWithThumbnailPlugin

This plugin has an Image plus additional commonly-used metadata:

* main image (with height and width)
* thumbnail image (with height and width)
* caption text (can be HTML content)
* credit/copyright text

Note that the thumbnail image and the main image do not have to be the same (i.e., that the thumbnail is just a resized version of the main image).

### 2.2.2. HostedVideoPlugin

This is a generic video container.   Each video is attached to a HostService (e.g., YouTube, Vimeo, etc.) and has a unique ID at that service, plus additional metadata:

* Title
* Duration
* Description

## 2.3. Really Special Plugins

These plugins were created for past projects.

### 2.3.1. BiographyPlugin

Biography container with headshot, byline, and bio.

### 2.3.2.  CountdownClockPlugin

Displays the time until a future date/time.

Fields available:

* t_minus = time as a `datetime.timedelta` (days, seconds, microseconds)
* total_seconds = "How many seconds are left?"
* in_the_past = "are we past the deadline"
* t_minus_days, t_minus_hours, t_minus_minutes, t_minus_seconds = the time left so you can format is as 3d 14h 32m 06s if you wanted to
* unixtime = the countdown "zero point" expressed as a UNIXTIME (e.g., 1550762809) - useful for some Javascript libraries (see below).
* unixtime_now = the time of the page load as a UNIXTIME

Note that this plugin does NOT include the functionality to provide a real-time counting down.   For that you'd need to install a Javascript library and create a custom renderer (see below) to run it, using some of the fields above to "seed" it.   (There are several different JS libraries for this out there.)


### 2.3.3. CompareTwoThingsPlugin

This basically allows for a side-by-side comparison of two things, e.g., "Let's Compare Wolverine vs. Cyclops".

# 3.0. Customization - Adding Renderers

You can create your own renderers for any of these plugins.

In your `settings.py` file, you need to add the `ADDITIONAL_PLUGIN_RENDERER_TEMPLATES` dict.   It has the following format:

```
ADDITIONAL_PLUGIN_RENDERER_TEMPLATES = {
    'GenericButtonPlugin':
        [
            (   'my_special_button',
                'Special Button',
                'foo_templates/special_button.html',
                'Use this renderer if you want things to be REALLY special.'
            ),
        ],
}
```

Each key in `ADDITIONAL_PLUGIN_RENDERER_TEMPLATES` is one of the custom plugins.  The value is a list of tuples, each of which is a renderer for that plugin.  So you can create as many as you'd like.

The tuple has 4 items:

1. The slug for the renderer;
2. The title (shown on the renderer dropdown when you're using the plugin);
3. The location of the rendering template;
4. Some descriptive help text about how this renderer works.

At present you can't remove any of the built-in renderers.

# Testing

TBD.

# Troubleshooting

TBD.

# Features still to be integrated

TBD.