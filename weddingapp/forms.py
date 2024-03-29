from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Event, Guest
from django.core.exceptions import ValidationError
from slugify import slugify


class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']


class EditEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']


class AddGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = [
            'email', 'event', 'attending', 'plus_one_attending',
            'invited', 'message_to_couple'
            ]
        fields = ['guest_name', 'user']
        widgets = {
            'guest_name': forms.TextInput(attrs={
                'id': 'guest-name',
                'required': True,
                'placeholder': "Enter your guest's name..."
            }),
            'user': forms.HiddenInput()
            }


class EditGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user', 'slug', 'message_to_couple', 'event']
