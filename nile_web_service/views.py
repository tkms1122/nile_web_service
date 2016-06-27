from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from ec2.views import SignupForm, LoginForm

def welcome(request):
    if request.user.is_authenticated():
        return redirect('ec2:root')
    s_form = UserForm()
    l_form = LoginForm()
    return render_to_response('nile_web_service/index.html', {'singup': s_form,'login' : l_form}, context_instance=RequestContext(request))

