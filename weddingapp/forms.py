from django import forms
from django.forms import ModelForm
from .models import Event, Guest


class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']


class addGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = [
            'user', 'email', 'event', 'attending', 'plus_one_attending',
            'message_to_couple', 'invited'
            ]
        fields = ['guest_name']
        widgets = {
            'guest_name': forms.TextInput(attrs={
                'id': 'guest-name',
                'required': True,
                'placeholder': "Enter your guest's name..."
            }),
        }


class editGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user', 'slug', 'message_to_couple']
