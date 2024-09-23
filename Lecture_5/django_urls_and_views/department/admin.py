from django.contrib import admin

from django_urls_and_views.department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
