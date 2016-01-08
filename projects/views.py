# views.py
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import get_object_or_404 as find
from django.utils import timezone

from .shortcuts import render_for

from .models import Project, Task
from .forms import ProjectForm, TaskForm, ToggleTaskForm


render_html = render_for('projects', '.html')
render_js   = render_for('projects', '.js', 'application/javascript')


def _ctx(project, **kwargs):
    kwargs['project'] = project
    # count the number of remaining tasks
    if 'remaining_tasks_count' not in kwargs:
        kwargs['remaining_tasks_count'] = project.remaining_tasks_count()
    # count the number of completed tasks
    if 'completed_tasks_count' not in kwargs:
        kwargs['completed_tasks_count'] = project.completed_tasks_count()
    return kwargs


@ensure_csrf_cookie
@require_http_methods(['GET'])
def index(request):
    projects = Project.objects.all()
    return render_html(request, 'index', { 'projects': projects })


@ensure_csrf_cookie
@require_http_methods(['GET'])
def show(request, pk, filter='all'):
    project = find(Project, pk=pk)
    context = { 'filter': filter }

    # retrieve project tasks with the specified filter
    if filter == 'active':
        context['tasks'] = project.task_set.active()
        # prevent a new db hit to count remaining tasks
        context['remaining_tasks_count'] = len(context['tasks'])
    elif filter == 'completed':
        context['tasks'] = project.task_set.completed()
        # prevent a new db hit to count completed tasks
        context['completed_tasks_count'] = len(context['tasks'])
    else:
        context['tasks'] = project.task_set.all()

    return render_html(request, 'show', _ctx(project, **context))


@require_http_methods(['POST'])
def create(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return render_js(request, 'create', { 'project': project })
    else:
        return HttpResponseBadRequest()


@require_http_methods(['PUT'])
def update(request, pk):
    project = find(Project, pk=pk)
    form = ProjectForm(request.PUT, instance=project)
    if form.is_valid():
        project = form.save(commit=False)
        project.save(update_fields=['name'])
    else:
        project.name = form.initial['name'] # reset changes
    return render_js(request, 'update', { 'project': project })


@require_http_methods(['DELETE'])
def delete(request, pk):
    project = find(Project, pk=pk)
    project.delete()
    return render_js(request, 'delete', { 'pk': pk })


@require_http_methods(['DELETE'])
def clear_completed(request, pk):
    project = find(Project, pk=pk)
    query = project.task_set.completed()
    task_ids = list(query.values_list('pk', flat=True))
    query.delete()
    return render_js(request, 'clear_completed', _ctx(project, task_ids=task_ids))


@require_http_methods(['PUT'])
def toggle_all(request, pk):
    project = find(Project, pk=pk)
    completed = (request.PUT.get('completed', '0') == '1')
    query = project.task_set.filter(completed=not(completed))
    task_ids = list(query.values_list('pk', flat=True))
    query.update(completed=completed, updated_at=timezone.now())
    return render_js(request, 'toggle_all', _ctx(project, completed=completed, task_ids=task_ids))


@require_http_methods(['POST'])
def create_task(request, project_id):
    task = Task(project_id=project_id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        task = form.save()
        return render_js(request, 'task_create', _ctx(task.project, task=task))
    else:
        return HttpResponseBadRequest()


@require_http_methods(['PUT'])
def update_task(request, pk, project_id):
    # fetch the task and verify the relationship (pk/project_id)
    task = find(Task, pk=pk, project_id=project_id)
    form = TaskForm(request.PUT, instance=task)
    if form.is_valid():
        task = form.save(commit=False)
        task.save(update_fields=['title'])
    elif not form.data.get('title', '').strip(): # empty title, just delete the task
        task.delete()
        return render_js(request, 'task_delete', _ctx(task.project, pk=pk))
    else:
        task.title = form.initial['title'] # reset changes
    return render_js(request, 'task_update', { 'task': task })


@require_http_methods(['PUT'])
def toggle_task(request, pk, project_id):
    # fetch the task with the related project and verify the relationship (pk/project_id)
    task = find(Task.objects.select_related('project'), pk=pk, project_id=project_id)
    form = ToggleTaskForm(request.PUT, instance=task)
    if form.is_valid():
        task = form.save(commit=False)
        task.save(update_fields=['completed'])
        return render_js(request, 'task_toggle', _ctx(task.project, task=task))
    else:
        return HttpResponseBadRequest()


@require_http_methods(['DELETE'])
def delete_task(request, pk, project_id):
    # fetch the task with the related project and verify the relationship (pk/project_id)
    task = find(Task.objects.select_related('project'), pk=pk, project_id=project_id)
    task.delete()
    return render_js(request, 'task_delete', _ctx(task.project, pk=pk))
