from django.forms import ModelForm
from .models import Event, Guest


class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']


class createGuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['guest_name', 'email']


class editGuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user', 'slug']
