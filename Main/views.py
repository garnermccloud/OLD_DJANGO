# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from Main.forms import UserCreateForm

def main_page(request):
    return render_to_response('main.html',context_instance=RequestContext(request))

def register_success(request):
    return  render_to_response('register_success.html',context_instance=RequestContext(request))

@login_required
def my_account(request):
    return  render_to_response('my_account.html', context_instance=RequestContext(request))

@login_required
def index(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    return render_to_response('home.html',context_instance=RequestContext(request))

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/register_success")
    else:
        form = UserCreateForm()
    con = {'form': form}
    con.update(csrf(request))

    return render_to_response("registration/register.html",con,context_instance=RequestContext(request))