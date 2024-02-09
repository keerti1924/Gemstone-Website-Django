from django.contrib.auth.models import  User
from .models import *
from django import forms

from django.forms.models import ModelForm
from django.forms.widgets import FileInput


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_image' : FileInput(),
        }

