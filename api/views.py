from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Project
from .serializers import ProjectSerializer

# from django.http import JsonResponse


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/projects/'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'}
    ]
    return Response(routes)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    print(serializer)
    return Response(serializer.data)
