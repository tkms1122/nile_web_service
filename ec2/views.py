from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.context_processors import csrf
from .models import Machine
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def machines_index(request):
    machines = Machine.objects.all()
    return render_to_response('ec2/machines/index.html', {'machines': machines} , context_instance=RequestContext(request))

def machines_launcher(request):
    if request.user.is_authenticated():
        return render_to_response('ec2/machines/launcher.html', None, context_instance=RequestContext(request))
    else:
        return redirect('ec2:root')

def machines_launch(request):
    if request.user.is_authenticated() & (request.method=="POST"):
        machine_name=request.POST['machine_name']
        cpu_core=request.POST['cpu_core']
        memory_size=request.POST['memory']
        m = Machine(owner=request.user.username, name=machine_name, core=cpu_core, memory=memory_size, status=0)
        m.save()
    return redirect('ec2:root')
    
