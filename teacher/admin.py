from django.contrib import admin

from teacher.models import Teacher, Address


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_id', 'gender', 'date_of_birth', 'joining_date',
                    'mobile_number']
    list_filter = ('gender', 'joining_date')
    search_fields = ['teacher_id', 'gender']
    readonly_fields = ['teacher_image']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'province', 'zip_code', 'country']
    list_filter = ('city', 'zip_code', 'country')
    search_fields = ['address', 'city', 'province', 'zip_code', 'country']
