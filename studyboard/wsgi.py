"""WSGI configuration for the Study Resources Board project."""
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studyboard.settings")

application = get_wsgi_application()
