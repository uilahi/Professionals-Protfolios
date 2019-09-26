from django.urls import path, include

from Python_Django.protfolio_second_project.blog import views


urlpatterns = [
    path("", views.allblogs, name='allblogs'),
    path("<int:blog_id>/", views.detail, name="detail")

    ]

