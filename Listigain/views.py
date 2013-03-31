# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.template.context import RequestContext
from Listigain.models import Task
from Listigain.models import TaskForm
from django.utils import simplejson
from time import time


@login_required
def index(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    educational_task_list = Task.objects.filter(user=request.user, category="EDU")
    social_task_list = Task.objects.filter(user=request.user, category="SOC")
    physical_task_list = Task.objects.filter(user=request.user, category="PHY")
    personal_task_list = Task.objects.filter(user=request.user, category="PER")
    return render_to_response('listigain.html',{'educational_task_list': educational_task_list,
                                                'social_task_list': social_task_list,
                                                'physical_task_list': physical_task_list,
                                                'personal_task_list': personal_task_list,},
        context_instance=RequestContext(request))

@login_required
def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TaskForm(request.POST)
        if form.is_valid() : # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            Task = form.save(commit=False)
            Task.user = request.user
            Task.save()
            return HttpResponseRedirect('/listigain') # Redirect after POST
    else:
        form = TaskForm()

    return render(request, 'addtask.html', {
        'form': form,
        })

@login_required
def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if  request.user == task.user:
        if request.method == 'POST': # If the form has been submitted...
            form = TaskForm(request.POST, instance=task)
            if form.is_valid() : # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
                form.save()
                return HttpResponseRedirect('/listigain') # Redirect after POST
        else:
            form = TaskForm(instance=task)

        return render(request, 'edittask.html', {
            'form': form,
            'task': task,
            })
    else:
        return HttpResponseRedirect('/listigain')

@login_required
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        if  request.user == task.user:
            task.delete()
    return HttpResponseRedirect('/listigain/')



# pick 4 tasks from users task list and display them.
@login_required
def initialize_quad(request):
    """
    make user list with user's tasks sorted by priority
    """
    user_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-priority','category')
    quad_tasks = list()
    for i in range(0,5):
        empty = {
        'id': -1,
        'content': "empty",
        'index': i
        }
        quad_tasks.append(empty)

    #make user list with user's tasks sorted by priority
    count = 0
    for task in user_tasks:
        quad_tasks[count]['id'] = task.pk
        quad_tasks[count]['content'] = task.content
        quad_tasks[count]['index'] = count
        count+=1
        if count==5:
            break




    # return the id, content, and index of each tasks in the quad in a JSON response
    return HttpResponse(simplejson.dumps(quad_tasks), mimetype='application/json')

@login_required
def return_quad(request, task_id):
    """
    make user list with user's tasks sorted by priority
    """
    #returned task is now completed so mark it completed in the database
    completed_task = get_object_or_404(Task, pk=task_id)
    if completed_task.user == request.user:
        Task.objects.filter(id=completed_task.pk).update(completed=True)



    user_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-priority','category')
    quad_tasks = list()
    for i in range(0,5):
        empty = {
            'id': -1,
            'content': "empty",
            'index': i
        }
        quad_tasks.append(empty)

    #make user list with user's tasks sorted by priority
    count = 0
    for task in user_tasks:
        quad_tasks[count]['id'] = task.pk
        quad_tasks[count]['content'] = task.content
        quad_tasks[count]['index'] = count
        count+=1
        if count==5:
            break



    # return the id, content, and index of each tasks in the quad in a JSON response
    return HttpResponse(simplejson.dumps(quad_tasks), mimetype='application/json')


