from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes.show', kwargs={'pk': self.pk})

