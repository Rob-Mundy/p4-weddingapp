from django.shortcuts import render
from django.views import generic
from .models import Guest
from .models import Event
from .models import User


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_name')
    template_name = 'index.html'


class GuestList(generic.ListView):
    model = Guest
    # my_guests = Guest.objects.filter(user=User.objects.get(username=request.user))
    queryset = Guest.objects.order_by('guest_name')
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Guest.objects.filter(user=user)
