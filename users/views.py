from django.urls import reverse_lazy

from .forms import UserLoginForm, PasswordChangeForm, UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView, TemplateView, PasswordChangeView, \
    PasswordChangeDoneView

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    success_message = 'You are successfully logged in'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'home'


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'users/password_change_form.html'


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    login_url = 'login'


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    success_message = 'Registration is completed. Please Login in here'
