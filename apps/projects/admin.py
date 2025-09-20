from django.contrib import admin
from .models import Project, ProjectFile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','display_count_of_files')
    search_fields = ('name',)
    list_filter = ('created_at',)

    def display_count_of_files(self, obj):
        return obj.count_files
    display_count_of_files.short_description = 'Count of files'

    @admin.action(description='Replace spaces with underscore in names')
    def replace_spaces_to_underscore(self, request, queryset):
        for obj in queryset:
            obj.name = obj.name.replace(' ', '_')
            obj.save()

    actions = [replace_spaces_to_underscore]


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
