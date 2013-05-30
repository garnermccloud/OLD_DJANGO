# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.template.context import RequestContext
from Listigain.models import Task, Start_Time, End_Time, TaskForm
from django.utils import simplejson
import datetime
import math
from time import time


@login_required
def index(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    school_task_list = Task.objects.filter(user=request.user,completed=False, category="SCH")
    school_time_worked = 0.0;
    for task in school_task_list:
        start_time_list = Start_Time.objects.filter(task=task).order_by('-time')
        end_time_list = End_Time.objects.filter(task=task).order_by('-time')
        st_list = list()
        end_list = list()
        for start_time in start_time_list:
            st_list.append(start_time.time)
        for end_time in end_time_list:
            end_list.append(end_time.time)
        for i in range(len(st_list)):
            session_delta = end_list[i] - st_list[i]
            session_seconds = session_delta.total_seconds()
            school_time_worked = school_time_worked + session_seconds


    misc_task_list = Task.objects.filter(user=request.user,completed=False, category="MIS")
    misc_time_worked = 0.0;
    for task in misc_task_list:
        start_time_list = Start_Time.objects.filter(task=task).order_by('-time')
        end_time_list = End_Time.objects.filter(task=task).order_by('-time')
        st_list = list()
        end_list = list()
        for start_time in start_time_list:
            st_list.append(start_time.time)
        for end_time in end_time_list:
            end_list.append(end_time.time)
        for i in range(len(st_list)):
            session_delta = end_list[i] - st_list[i]
            session_seconds = session_delta.total_seconds()
            misc_time_worked =  misc_time_worked + session_seconds


    school_time_worked_hours = int(math.floor(school_time_worked/3600))
    school_time_worked = school_time_worked - (school_time_worked_hours*3600)
    school_time_worked_minutes = int(math.floor(school_time_worked/60))
    school_time_worked = school_time_worked - (school_time_worked_minutes*60)
    school_time_worked_seconds = int(math.floor(school_time_worked))
            
    misc_time_worked_hours = int(math.floor(misc_time_worked/3600))
    misc_time_worked = misc_time_worked - (misc_time_worked_hours*3600)
    misc_time_worked_minutes = int(math.floor(misc_time_worked/60))
    misc_time_worked = misc_time_worked - (misc_time_worked_minutes*60)
    misc_time_worked_seconds = int(math.floor(misc_time_worked))



    return render_to_response('listigain.html',{'school_task_list': school_task_list,
                                                'misc_task_list': misc_task_list,
                                                'school_time_worked_hours': school_time_worked_hours,
                                                'school_time_worked_minutes': school_time_worked_minutes,
                                                'school_time_worked_seconds': school_time_worked_seconds,
                                                'misc_time_worked_hours': misc_time_worked_hours,
                                                'misc_time_worked_minutes': misc_time_worked_minutes,
                                                'misc_time_worked_seconds': misc_time_worked_seconds,},
        context_instance=RequestContext(request))


def index_completed(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    school_task_list = Task.objects.filter(user=request.user,completed=True, category="SCH")
    misc_task_list = Task.objects.filter(user=request.user,completed=True, category="MIS")
    return render_to_response('listigain_completed.html',{'school_task_list': school_task_list,
                                                'misc_task_list': misc_task_list,},
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
    user_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-importance','enjoyment')
    quad_tasks = list()
    for i in range(0,5):
        empty = {
        'id': -1,
        'content': "empty",
        'complete_percentage': 0,
        'index': i
        }
        quad_tasks.append(empty)

    #make user list with user's tasks sorted by priority
    count = 0
    for task in user_tasks:
        quad_tasks[count]['id'] = task.pk
        quad_tasks[count]['content'] = task.content
        quad_tasks[count]['complete_percentage'] = task.complete_percentage
        quad_tasks[count]['index'] = count
        count+=1
        if count==5:
            break




    # return the id, content, and index of each tasks in the quad in a JSON response
    return HttpResponse(simplejson.dumps(quad_tasks), mimetype='application/json')

@login_required
def completed(request, task_id, start_time, end_time):
    """
    make user list with user's tasks sorted by priority
    """
    #returned task is now completed so mark it completed in the database
    completed_task = get_object_or_404(Task, pk=task_id)
    if completed_task.user == request.user:
        start_time = float(start_time)
        start_time = datetime.datetime.fromtimestamp(start_time/1000.0)
        time_started = Start_Time(time=start_time, task = completed_task)
        time_started.save()

        end_time = float(end_time)
        end_time = datetime.datetime.fromtimestamp(end_time/1000.0)
        time_end = End_Time(time=end_time, task = completed_task)
        time_end.save()
        Task.objects.filter(id=completed_task.pk).update(completed=True)




    user_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-importance','enjoyment')
    quad_tasks = list()
    for i in range(0,5):
        empty = {
            'id': -1,
            'content': "empty",
            'complete_percentage': 0,
            'index': i
        }
        quad_tasks.append(empty)

    #make user list with user's tasks sorted by priority
    count = 0
    for task in user_tasks:
        quad_tasks[count]['id'] = task.pk
        quad_tasks[count]['content'] = task.content
        quad_tasks[count]['complete_percentage'] = task.complete_percentage
        quad_tasks[count]['index'] = count
        count+=1
        if count==5:
            break



    # return the id, content, and index of each tasks in the quad in a JSON response
    return HttpResponse(simplejson.dumps(quad_tasks), mimetype='application/json')


@login_required
def completed_from_listigain(request, task_id, start_time, end_time):
    """
    make user list with user's tasks sorted by priority
    """
    #returned task is now completed so mark it completed in the database
    completed_task = get_object_or_404(Task, pk=task_id)
    if completed_task.user == request.user:
        start_time = float(start_time)
        start_time = datetime.datetime.fromtimestamp(start_time/1000.0)
        time_started = Start_Time(time=start_time, task = completed_task)
        time_started.save()

        end_time = float(end_time)
        end_time = datetime.datetime.fromtimestamp(end_time/1000.0)
        time_end = End_Time(time=end_time, task = completed_task)
        time_end.save()
        Task.objects.filter(id=completed_task.pk).update(completed=True)
        return HttpResponseRedirect('/listigain/quad/completed_break')
    else:
        return HttpResponseRedirect('/listigain/')



@login_required
def time_up(request, task_id, start_time, end_time):
    """
    make user list with user's tasks sorted by priority
    """
    #returned task is now completed so mark it completed in the database
    completed_task = get_object_or_404(Task, pk=task_id)
    if completed_task.user == request.user:
        start_time = float(start_time)
        start_time = datetime.datetime.fromtimestamp(start_time/1000.0)
        time_started = Start_Time(time=start_time, task = completed_task)
        time_started.save()

        end_time = float(end_time)
        end_time = datetime.datetime.fromtimestamp(end_time/1000.0)
        time_end = End_Time(time=end_time, task = completed_task)
        time_end.save()



    user_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-importance','enjoyment')
    quad_tasks = list()
    for i in range(0,5):
        empty = {
            'id': -1,
            'content': "empty",
            'complete_percentage': 0,
            'index': i
        }
        quad_tasks.append(empty)

    #make user list with user's tasks sorted by priority
    count = 0
    for task in user_tasks:
        quad_tasks[count]['id'] = task.pk
        quad_tasks[count]['content'] = task.content
        quad_tasks[count]['complete_percentage'] = task.complete_percentage
        quad_tasks[count]['index'] = count
        count+=1
        if count==5:
            break



    # return the id, content, and index of each tasks in the quad in a JSON response
    return HttpResponse(simplejson.dumps(quad_tasks), mimetype='application/json')


@login_required
def time_up_from_listigain(request, task_id, start_time, end_time):
    """
    make user list with user's tasks sorted by priority
    """
    #returned task is now completed so mark it completed in the database
    completed_task = get_object_or_404(Task, pk=task_id)
    if completed_task.user == request.user:
        start_time = float(start_time)
        start_time = datetime.datetime.fromtimestamp(start_time/1000.0)
        time_started = Start_Time(time=start_time, task = completed_task)
        time_started.save()

        end_time = float(end_time)
        end_time = datetime.datetime.fromtimestamp(end_time/1000.0)
        time_end = End_Time(time=end_time, task = completed_task)
        time_end.save()
        return HttpResponseRedirect('/listigain/quad/time_up_break')
    else:
        return HttpResponseRedirect('/listigain/')






@login_required
def quad_from_listigain(request, task_id):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """

    requested_task = get_object_or_404(Task, pk=task_id)
    if requested_task.user == request.user:
            return render_to_response('quad_from_listigain.html',{'requested_task': requested_task,},
                context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/listigain/')

