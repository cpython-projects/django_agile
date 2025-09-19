from django.db import models
from django.core.validators import MinValueValidator

from django.contrib.auth.models import User
from django.utils import timezone

# class Created(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         abstract = True

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinValueValidator(4)])
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name