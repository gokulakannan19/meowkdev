from django.core import paginator
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Project, Review, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProject, paginateProjects


def projects(request):

    projects, search_query = searchProject(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {
        'projects': projects,
        'search_query': search_query,

        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)

    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()

            project.get_vote_ratio

            messages.success(request, "Your review is successfully submitted")
            return redirect('project', pk=project.id)

    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'projects/single-project.html', context)


@ login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {
        'form': form,
    }
    return render(request, 'projects/project-form.html', context)


@ login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form,
    }
    return render(request, 'projects/project-form.html', context)


@ login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('account')
    context = {
        "object": project
    }

    return render(request, 'delete-template.html', context)
