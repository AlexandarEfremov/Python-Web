from django.urls import path

from django_urls_and_views.department import views

urlpatterns = [
    path("department/", views.index)
]