from django.contrib import admin

from department.models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'name', 'head_of_department',
                    'start_date']
    list_filter = ('department_id', 'start_date')
    search_fields = ['department_id', 'name']
