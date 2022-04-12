"""
WSGI config for dncproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dncproject.settings')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()