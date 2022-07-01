"""
    proyecto/wsgi.py: 
                        Un punto de entrada para que los servidores web compatibles con WSGI puedan servir su proyecto
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primera_app_django.settings')

application = get_wsgi_application()
