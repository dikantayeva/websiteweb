"""
WSGI config for employee_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
python -m pip install uwsgi
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_management.settings')

application = get_wsgi_application()
