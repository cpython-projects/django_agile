#
# from django.contrib import admin
# from .models import Project, ProjectFile
#
#
#
#
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     verbose_name = 'Project'
#     verbose_name_plural = 'Projects'
#     list_display = ('name','display_count_of_files')
#     search_fields = ('name','created')
#
#     def display_count_of_files(self, obj):
#         return obj.count_files
#     display_count_of_files.short_description = 'Count of files'
#
#     @admin.action(description='Display count of files')
#     def replace_spaces_to_underscore(self, request, objects):
#         for obj in objects:
#             obj.name = obj.name.replace(' ', '_')
#             obj.save()
#         return objects
#
#     actions = [replace_spaces_to_underscore]
#
#
# @admin.register(ProjectFile)
# class ProjectFileAdmin(admin.ModelAdmin):
#     list_display = ('name', 'file', 'created_at')
#     search_fields = ('name',)
#     list_filter = ('created_at',)
#
