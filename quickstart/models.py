from django.db import models
from django.utils import timezone

# Create your models here.

class URL(models.Model):
    label = models.CharField(null=True, blank=True, max_length=30)
    address = models.URLField()
    slug = models.SlugField(unique=True, max_length=8)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label