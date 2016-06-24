from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class AccountCreateView(CreateView):
    model = User

    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('ec2:root')
