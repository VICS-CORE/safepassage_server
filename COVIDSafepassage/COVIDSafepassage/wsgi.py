"""
WSGI config for COVIDSafepassage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import traceback as tb
import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'COVIDSafepassage.settings')

try:
        application = get_wsgi_application()
except Exception as e:
        print(sys.path)
        tb.print_exc()
