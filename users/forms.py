from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control',
                                                       'id': 'username',
                                                       }))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                           'id': 'password',
                                                           }))


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                               'id': 'old_password',
                                                               }))
    new_password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                                'id': 'new_password1',
                                                                }))
    new_password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                                'id': 'new_password2',
                                                                }))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control',
                                                       'id': 'username',
                                                       }))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                            'id': 'password1',
                                                            }))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                            'id': 'password2',
                                                            }))
