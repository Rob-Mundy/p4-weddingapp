from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Guest, Event, User
from django.conf import settings
from .forms import CreateEventForm, EditEventForm, AddGuestForm, EditGuestForm
from slugify import slugify
from django.core.exceptions import ValidationError
from django.db.models import Count


class EventList(generic.ListView):
    model = Event
    template_name = 'index.html'
    context_object_name = 'events'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            return Event.objects.filter(user=user)

    def get_context_data(self, *args, **kwargs):
        user = self.request.user
        context = super(EventList, self).get_context_data(*args, **kwargs)
        if user.is_authenticated:
            # filters event objects by user and counts guests
            context['event_stats'] =
            Event.objects.filter(user=user).aggregate(Count('guests'))
            return context


class GuestList(generic.View):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        # 404 error if user navigates to guestlist but has no event
        event = get_object_or_404(Event, user=user)
        queryset = Guest.objects.filter(user=user)
        context_object_name = 'guests'
        form = AddGuestForm(request.POST or None, initial={'user': user.id})

        return render(
            request,
            "guestlist.html",
            {
                "form": form,
                "guests": queryset
            }
        )

    def post(self, request, *args, **kwargs):
        user = self.request.user
        # 404 error if user triest to access events that
        # belong to other users
        event = get_object_or_404(Event, user=user)
        form = AddGuestForm(data=request.POST, initial={'user': user.id})
        if form.is_valid():
            guest_list = form.save(commit=False)
            guest_list.user = user
            # slug field added based on concatonation of user_id
            # and guest_name so that guest can be accessed by slug
            # for editing
            guest_list.slug =
            slugify(str(guest_list.user.id) + '-' + guest_list.guest_name)

            guest_list.event = event
            guest_list.save()
            form.save(commit=True)
            return redirect("guestlist")

        return render(
            request,
            "guestlist.html",
            {
                "form": form,
            }
        )


class GuestDetail(generic.View):

    def get(self, request, slug, *args, **kwargs):
        user = self.request.user
        queryset = Guest.objects.filter(user=user)
        instance = get_object_or_404(queryset, slug=slug)
        form = EditGuestForm(request.POST or None, instance=instance)

        return render(
            request,
            "edit_guest.html",
            {
                "instance": instance,
                "form": form,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        user = self.request.user
        queryset = Guest.objects.filter(user=user)
        instance = get_object_or_404(queryset, slug=slug)
        form = EditGuestForm(data=request.POST, instance=instance)
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


def delete_guest(request, pk):
    queryset = Guest.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect("guestlist")
    return render(request, 'delete_guest.html')


def create_event(request):
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event_list = form.save(commit=False)
            event_list.user = request.user
            event_list.save()
            form.save(commit=True)
            return redirect('/')
    else:
        form = CreateEventForm()
    return render(request, 'create_event.html', {'form': form})


class EventDetail(generic.UpdateView):

    def get(self, request, pk):
        user = self.request.user
        queryset = Event.objects.filter(user=user)
        instance = get_object_or_404(queryset, pk=pk)
        form = EditEventForm(request.POST or None, instance=instance)

        return render(
            request,
            "edit_event.html",
            {
                "instance": instance,
                "form": form
            }
        )

    def post(self, request, pk):
        user = self.request.user
        queryset = Event.objects.filter(user=user)
        instance = get_object_or_404(queryset, pk=pk)
        form = EditEventForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("/")

        return render(
            request,
            "edit_event.html",
            {
                "instance": instance,
                "form": form
            }
        )
