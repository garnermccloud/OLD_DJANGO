# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.template.context import RequestContext
from Listigain.models import Task
from Listigain.models import TaskForm


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
    return render_to_response('Listigain.html',{'educational_task_list': educational_task_list,
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
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        if  request.user == task.user:
            task.delete()
    return HttpResponseRedirect('/listigain/')
