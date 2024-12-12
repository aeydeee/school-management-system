from django.contrib import admin

from class_group.models import Class, Section


# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'section']
    list_filter = ('name', 'subject')
    search_fields = ['subject', 'name', 'section']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['grade_level', 'name']
    list_filter = ('name', 'grade_level')
    search_fields = ['grade_level', 'name']
