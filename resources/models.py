"""Database models for learning resources."""
from django.db import models


class StudyResource(models.Model):
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=60)
    url = models.URLField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
