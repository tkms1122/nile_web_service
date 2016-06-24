from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AccountCreateView(CreateView):
    model = User

    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('my:user_creation')
