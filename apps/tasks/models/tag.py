from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(4)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
