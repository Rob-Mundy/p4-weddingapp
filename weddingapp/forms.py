from django import forms
from django.forms import ModelForm
from .models import Event, Guest
from django.core.exceptions import ValidationError
from slugify import slugify


class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']


class editEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']


class addGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = [
            'email', 'event', 'attending', 'plus_one_attending',
            'message_to_couple', 'invited'
            ]
        fields = ['guest_name']
        widgets = {
            'guest_name': forms.TextInput(attrs={
                'id': 'guest-name',
                'required': True,
                'placeholder': "Enter your guest's name..."
            })
        }

    def clean_guest_name(self):  # ensures no slugfield duplications by slugifying guest_name
        guest_name = self.cleaned_data.get('guest_name')

        for guest in Guest.objects.all():
            if slugify(str(guest.user.pk) + '-' + guest.guest_name) == slugify(str(guest.user.pk) + '-' + guest_name):
                raise forms.ValidationError('There is already a guest called ' + guest_name)
        return guest_name


class editGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user', 'slug', 'message_to_couple']
