from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ec2.views import SignupForm, LoginForm
from django.core.urlresolvers import reverse

class AccountCreateView(CreateView):
    model = User

    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('my:user_creation')

def signup(request):
    if request.user.is_authenticated():
        return redirect('ec2:root')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_name=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = User.objects.create_user(username=user_name, password=password)
            user.save()
            return redirect('ec2:root')

    # if a GET (or any other method) we'll create a blank form
    return redirect('ec2:root')

def log_in(request):
    if request.user.is_authenticated():
        return redirect('ec2:root')
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
    return redirect('ec2:root')

