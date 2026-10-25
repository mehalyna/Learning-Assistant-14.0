"""ASGI configuration for the Study Resources Board project."""
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studyboard.settings")

application = get_asgi_application()
