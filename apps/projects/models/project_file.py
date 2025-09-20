from django.db import models

# Create your models here.
class ProjectFile(models.Model):
    name = models.CharField(max_length=120)
    file = models.FileField(upload_to='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'