from django.shortcuts import render


# Create your views here.


def projects(req):
    return render(req, "projects.html")


def agriculture(req):
    return render(req, "agriculture.html")
