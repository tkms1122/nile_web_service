from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render_to_response('nile_web_service/index.html', None, context_instance=RequestContext(request))

