"""Admin configuration for learning resources."""
from django.contrib import admin

from .models import StudyResource


admin.site.register(StudyResource)
