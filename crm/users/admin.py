from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Student


@admin.register(Student)
class StudentAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'student_id', 'group', 'is_active')
    list_filter = ('group', 'is_active', 'is_staff')
    search_fields = ('username', 'last_name', 'first_name', 'student_id')
    fieldsets = UserAdmin.fieldsets + (
        ('Данные студента', {'fields': ('middle_name', 'birth_date', 'phone', 'student_id', 'group')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Данные студента', {'fields': ('first_name', 'last_name', 'student_id', 'group')}),
    )
