from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Guest, Event, User
from django.core.mail import send_mail
from django.conf import settings
from .forms import createEventForm, editGuestForm


class EventList(generic.ListView):
    model = Event
    # queryset = Event.objects.order_by('event_name')
    template_name = 'index.html'
    context_object_name = 'events'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Event.objects.filter(user=user)
            # return user.events.all()


class GuestList(generic.ListView):
    model = Guest
    queryset = Guest.objects.order_by('guest_name')
    template_name = 'guestlist.html'
    context_object_name = 'guests'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Guest.objects.filter(user=user)
        # return user.guests.all()


def create_event(request):
    form = createEventForm()
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            event_list = form.save(commit=False)
            event_list.user = request.user
            event_list.save()
            form.save(commit=True)
            return redirect('/')
    else:
        form = createEventForm()
    return render(request, 'create_event.html', {'form': form})


class GuestDetail(generic.View):

    def get(self, request, slug, *args, **kwargs):
        user = self.request.user
        queryset = Guest.objects.filter(user=user)
        instance = get_object_or_404(queryset, slug=slug)
        form = editGuestForm(request.POST or None, instance=instance)
        # if form.is_valid():
        #     form.save()
        #     return redirect("edit_guest")

        return render(
            request,
            "edit_guest.html",
            {
                "instance": instance,
                "form": form
            }
        )

    def post(self, request, slug, *args, **kwargs):
        user = self.request.user
        queryset = Guest.objects.filter(user=user)
        instance = get_object_or_404(queryset, slug=slug)
        form = editGuestForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("guestlist")

        return render(
            request,
            "edit_guest.html",
            {
                "instance": instance,
                "form": form
            }
        )
