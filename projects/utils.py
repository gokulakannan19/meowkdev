from django.db.models import Q
from .models import Project, Review, Tag


def searchProject(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print("SEARCH QUERY: ", search_query)

    tag = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(owner__name__icontains=search_query) |
        Q(tags__in=tag))

    return projects, search_query
