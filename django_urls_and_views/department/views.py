from django.http import HttpResponse
from django.shortcuts import render

from django_urls_and_views.department.models import Department


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def view_with_name(request, variable):
    return render(request, "departments/name_template.html", {"variable": variable})