from django.urls import path, re_path

from django_urls_and_views.department import views

urlpatterns = [
    path("<variable>/", views.view_with_name),
    path("department/", views.index),
    path("<slug:slug>/", views.view_with_slug),

    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
]