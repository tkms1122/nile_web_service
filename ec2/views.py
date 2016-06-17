from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def machines_index(request):
    return render_to_response('ec2/machines/index.html', None , context_instance=RequestContext(request))
