from django.shortcuts import render
from .models import MiniProjectsModal

# Create your views here.


def projects(req):
    modal_data = MiniProjectsModal.objects.all()
    return render(req, "projects.html", {"miniprojects": modal_data})


def agriculture(req):
    return render(req, "agriculture.html")
