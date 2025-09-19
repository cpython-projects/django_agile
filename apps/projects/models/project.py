from django.db import models
from . import ProjectFile


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(ProjectFile, blank=True, related_name='projects')


    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-name',)
        unique_together = (('name', 'description'),)

    @property
    def count_files(self):
        return self.files.count()


    def __str__(self):
        return self.name