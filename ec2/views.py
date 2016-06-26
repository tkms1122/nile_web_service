from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.context_processors import csrf
from .models import Machine
from django.contrib.auth.decorators import login_required
import json
import uuid


@login_required(login_url="/")
def machines_index(request):
    machines = Machine.objects.all()
    return render_to_response('ec2/machines/index.html', {'machines': machines} , context_instance=RequestContext(request))

def machines_launch(request):
    def validate(name,core,mem,token):
        return (len(name) > 3)
    res = {}
    if request.user.is_authenticated():
        machine_token = uuid.uuid4()
        machine_name = request.GET['machine_name']
        cpu_core = request.GET['cpu_core']
        memory_size = request.GET['memory']
        isvalid = validate(machine_name, cpu_core, memory_size, machine_token)
        res['isvalid'] = isvalid
        if isvalid:
            m = Machine(auth_user=request.user, machine_token=machine_token, name=machine_name, core=cpu_core,
                        memory=memory_size, status=0)
            res['name'] = machine_name
            res['core'] = cpu_core
            res['stat'] = m.getstate()
            res['statcolor'] = m.getstatecolor()
            m.save()
    return HttpResponse(json.dumps(res))
    
