"""Forms for creating and updating learning resources."""
from django import forms

from .models import StudyResource


class StudyResourceForm(forms.ModelForm):
    class Meta:
        model = StudyResource
        fields = ["title", "subject", "url", "description"]
