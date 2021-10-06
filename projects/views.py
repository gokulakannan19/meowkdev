from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse("Here are the list of projects")


def project(request, pk):
    return HttpResponse(f"Single Project {pk}")
