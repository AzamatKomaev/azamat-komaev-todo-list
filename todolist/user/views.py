from django.contrib.auth.models import User
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLoginForm


class RegistrationView(View):
    http_method_names = ('get', 'post',)
    form = UserRegistrationForm()
    template_name = 'user/user_register.jinja'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        self.form = UserRegistrationForm(request.POST)
        if self.form.is_valid():
            user = User.objects.create_user(**self.form.cleaned_data)
            return redirect('task.list')

        return render(request, self.template_name, {'form': self.form})


class NotFoundTemplateView(TemplateView):
    template_name = 'user/error.not_found.jinja'


def show_not_found_error(request):
    template_name = 'user/error.not_found.jinja'
    return render(request, template_name, {})

