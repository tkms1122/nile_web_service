from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("Hello EC2!")

def tab(request):
    return render_to_response('ec2/tab.html', None , context_instance=RequestContext(request))