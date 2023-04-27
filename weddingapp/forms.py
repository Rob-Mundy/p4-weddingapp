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
            'invited', 'message_to_couple'
            ]
        fields = ['guest_name', 'user']
        widgets = {
            'guest_name': forms.TextInput(attrs={
                'id': 'guest-name',
                'required': True,
                'placeholder': "Enter your guest's name..."
            }),
            'user': forms.TextInput(attrs={
                'required': True,
            }),
        }

    def clean_guest_name(self):  # ensures no slugfield duplications by slugifying guest_name
        clean_guest_name = self.cleaned_data.get('guest_name')
        clean_user = self.cleaned_data.get('user')
        slugtest = slugify(str(clean_user) + '-' + clean_guest_name)
        for guest in Guest.objects.all():

            if guest.slug == slugtest:
                raise forms.ValidationError('There is already a guest called ' + clean_guest_name)
                
        return clean_guest_name


    # def clean_guests(self):  # ensures no slugfield duplications by slugifying guest_name
    #     # cleaned_data = super().clean()
    #     guest_name = self.cleaned_data.get('guest_name')
    #     user = self.cleaned_data.get('user')

    #     for guest in Guest.objects.get(user=user):
    #         if guest.guest_name == guest_name:
    #             raise forms.ValidationError('There is already a guest called ' + guest_name)
    #         print(guest_name)
    #     return guest_name


class editGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user', 'slug', 'message_to_couple']
