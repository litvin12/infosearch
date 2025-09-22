from django.contrib import admin
from .models import University, Student

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'established_date')
    search_fields = ('full_name', 'short_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'university', 'enrollment_year')
    search_fields = ('full_name',)
    list_filter = ('university', 'enrollment_year')
