import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms-stackable-plugins',
    version='0.3',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License, see LICENSE',
    description="DjangoCMS plugins designed for content producers.",
    long_description=README,
    long_description_content_type='text/markdown',
    url='http://github.com/wgbh/django-stackable-plugins/',
    author='Bob Donahue',
    author_email='bob_donahue@wgbh.org',
    install_requires=[
        'pytz', 'djangocms-attributes-field', 'django-colorfield'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
