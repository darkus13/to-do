from django.utils import timezone
from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=120, default=0)
    priority = models.CharField(max_length=120, default=0)
    deadline = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.title
