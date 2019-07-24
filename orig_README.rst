==========
Stackable Plugins
==========

A set of plugins for Django CMS.

Some are generic plugins to help define the framework of a page/placeholder.

Others provide generic content-handling (e.g., a generic video player, a countdown clock, etc.).

Each plugin has a set of one or more "renderer" templates;  you can create additional renderer templates to suit your own project's needs.

Quick start
-----------

1. Add "stackable_plugins" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gatekeeper',
    ]
    
2. run "manage.py migrate stackable_plugins"


See the project README for more-detailed instructions of use.
