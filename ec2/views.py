from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "ec2/index.html")

def container_view(request):
    return render(request, "ec2/container.html")

def jqr(request):
    return render(request, "ec2/jqr.html")