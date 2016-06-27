# coding: UTF-8

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.context_processors import csrf
from .models import Machine
from .models import IP
from django.contrib.auth.decorators import login_required
from django import forms
import json, uuid, os
import libvirt

class SignupForm(forms.Form):
    username = forms.CharField(required=True,label='Your name',max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=4)


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput(), min_length=4)

@login_required(login_url="/")
def machines_index(request):
    machines = Machine.objects.all()
    s_form = SignupForm()
    l_form = LoginForm()
    return render_to_response('ec2/machines/index.html', {'machines': machines,'singup': s_form,'login' : l_form} , context_instance=RequestContext(request))

# VM新規作成
def machines_launch(request):
    def validate(name,core,mem,token,ip):
        # TODO: invalidの理由を含める
        if ip == None:
            return False
        elif len(name) <= 3:
            return False
        else:
            return True

    res = {}
    if request.user.is_authenticated():
        machine_token = uuid.uuid4()
        machine_name = request.GET['machine_name']
        cpu_core = request.GET['cpu_core']
        memory_size = request.GET['memory']

        unusedIPs = IP.objects.filter(is_used=False)
        ip = unusedIPs[0] if len(unusedIPs) > 0 else None

        isvalid = validate(machine_name, cpu_core, memory_size, machine_token, ip)
        res['isvalid'] = isvalid
        if isvalid:
            #　machineテーブルに追加
            m = Machine(auth_user=request.user, ip=ip, machine_token=machine_token, name=machine_name, core=cpu_core, memory=memory_size, status=0)
            res['name'] = machine_name
            res['core'] = cpu_core
            res['stat'] = m.getstate()
            res['statcolor'] = m.getstatecolor()
            m.save()
            ip.is_used = True
            ip.save()

            # 鍵生成&VM立ち上げ
            ssh_key_name = '{0}_{1}'.format(request.user.username, machine_name)
            os.system('ssh-keygen -b 4096 -t rsa -N "" -f /tmp/{0}'.format(ssh_key_name))
            os.system('scp -i /home/nws/.ssh/id_rsa /tmp/{0}.pub nws@157.82.3.112:/tmp/{0}.pub'.format(ssh_key_name))
            os.system('rm /tmp/{0}.pub'.format(ssh_key_name))
            os.system('ssh -i /home/nws/.ssh/id_rsa nws@157.82.3.112 "sudo bash /home/nws/create.bash {vm_name} {pub_key} {ip}"'.format(
                vm_name = machine_token,
                pub_key = '/tmp/{0}.pub'.format(ssh_key_name),
                ip = ip.address
            ))
    return HttpResponse(json.dumps(res))

# VM 起動
def machines_start(request, machine_token):
    res = {}
    if request.user.is_authenticated():
        m = Machine.objects.get(machine_token=machine_token)
        con = libvirt.open("qemu+tls://157.82.3.112/system")
        dom = con.lookupByName(m.machine_token)
        info = dom.info()
        if info[0] != 1: #VIR_DOMAIN_RUNNING
            dom.create()
        m.status = 1
        m.save()
    return HttpResponse(json.dumps(res))

# VM 終了
def machines_stop(request, machine_token):
    res = {}
    if request.user.is_authenticated():
        m = Machine.objects.get(machine_token=machine_token)
        con = libvirt.open("qemu+tls://157.82.3.112/system")
        dom = con.lookupByName(m.machine_token)
        info = dom.info()
        if info[0] != 5: #VIR_DOMAIN_SHUTOFF
            dom.destroy()
        m.status = 0
        m.save()
    return HttpResponse(json.dumps(res))

# VM 削除
def machines_destroy(request, machine_token):
    if request.user.is_authenticated():
        m = Machine.objects.get(machine_token=machine_token)
        con = libvirt.open("qemu+tls://157.82.3.112/system")
        dom = con.lookupByName(m.machine_token)
        info = dom.info();
        if info[0] != 5: #VIR_DOMAIN_SHUTOFF
            dom.destroy()
        dom.undefine()
        ip = m.ip
        ip.is_used = False
        ip.save()
        m.delete()

    return HttpResponse('done')

def machines_downloadkey(request, machine_token):
    m = Machine.objects.get(machine_token=machine_token)
    private_key = '{0}_{1}'.format(request.user.username, m.name)
    response = HttpResponse(open('/tmp/{0}'.format(private_key),'rb').read(), content_type='text/plain')
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'filename={0}.pem'.format(private_key)
    os.system('rm /tmp/{0}'.format(private_key))
    return response

def machines_getlist(request):
    res = {}
    if request.user.is_authenticated():
        machines = Machine.objects.all()
        machines = filter(lambda m: m.auth_user.username == request.user.username, machines)
        for idx, m in enumerate(machines):
            instance = {
                    'username': m.auth_user.username,
                    'machine_token': m.machine_token,
                    'name': m.name,
                    'core': m.core,
                    'memory': m.memory,
                    'status': m.status
            }
            res[idx] = instance
        return HttpResponse(json.dumps(res))
    return HttpResponse(json.dumps(res))
