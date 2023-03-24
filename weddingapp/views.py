from django.shortcuts import render, redirect
from django.views import generic
from .models import Guest, Event, User
from django.core.mail import send_mail
from django.conf import settings
from .forms import createEventForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_name')
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Event.objects.filter(user=user)


class GuestList(generic.ListView):
    model = Guest
    queryset = Guest.objects.order_by('guest_name')
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Guest.objects.filter(user=user)


# def index(request):
#     form = createEventForm()
#     return render(request, 'index.html', {"form": form.as_p})

def create_event(request):
    form = createEventForm()
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('create_event.html')
    else:
        form = createEventForm()
    return render(request, 'create_event.html', {'form': form})
