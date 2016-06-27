from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ec2.views import UserForm, LoginForm
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
        s_form = UserForm(request.POST)
        # check whether it's valid:
        if s_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_name=s_form.cleaned_data['username']
            password=s_form.cleaned_data['password']
            user = User.objects.create_user(username=user_name, password=password)
            user.save()
            return redirect('ec2:root')
        else:
            l_form = LoginForm()
    else:
        s_form = UserForm()
        l_form = LoginForm()
    # if a GET (or any other method) we'll create a blank form
    return render_to_response('nile_web_service/index.html', {'singup': s_form,'login' : l_form}, context_instance=RequestContext(request))

def log_in(request):
    if request.user.is_authenticated():
        return redirect('ec2:root')
    if request.method=="POST":
        l_form = LoginForm(request.POST)
        if l_form.is_valid():
            username = l_form.cleaned_data['username']
            password = l_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('ec2:root')
    else:
        l_form = LoginForm()
    s_form = UserForm()
    return render_to_response('nile_web_service/index.html', {'singup': s_form,'login' : l_form}, context_instance=RequestContext(request))

