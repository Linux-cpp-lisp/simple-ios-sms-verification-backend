"""
WSGI config for sms_verification project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(0, '/var/www/sms_verification')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sms_verification.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
