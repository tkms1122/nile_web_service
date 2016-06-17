from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class AccountCreateView(CreateView):
    model = User

    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('my:user_creation')

class AccountUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm

    def get_success_url(self):
        return reverse('my:user_change', args=(self.object.id, ))
