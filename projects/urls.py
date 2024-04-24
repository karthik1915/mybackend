from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("smart-agriculture/", views.agriculture, name="agriculture"),
]
