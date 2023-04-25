from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Guest, Event, User
from django.core.mail import send_mail
from django.conf import settings
from .forms import createEventForm, addGuestForm, editGuestForm
from slugify import slugify

import json


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


# class GuestList(generic.ListView):
#     model = Guest
#     queryset = Guest.objects.order_by('guest_name')
#     template_name = 'guestlist.html'
#     context_object_name = 'guests'
#     form = addGuestForm()

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_authenticated:
#             return Guest.objects.filter(user=user)



# def home(req):
#     tmpl_vars = {
#         'all_guests': Guest.objects.reverse(),
#         'form': addGuestForm()
#     }
#     return render(req, 'index.html', tmpl_vars)


class GuestList(generic.View):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        queryset = Guest.objects.filter(user=user)
        context_object_name = 'guests'
        form = addGuestForm(request.POST or None)

        return render(
            request,
            "guestlist.html",
            {
                "form": form,
                "guests": queryset
            }
        )

    def post(self, request, *args, **kwargs):
        form = addGuestForm(data=request.POST)
        if form.is_valid():
            guest_list = form.save(commit=False)
            guest_list.user = request.user
            guest_list.slug = slugify(str(guest_list.user.id) + '-' + guest_list.guest_name)
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


def delete_guest(request, pk):
    queryset = Guest.objects.get(id=pk)
    name = Guest.guest_name
    if request.method == 'POST':
        queryset.delete()
        return redirect("guestlist")
    return render(request, 'delete_guest.html')

    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         user = self.request.user
    #         guest_name = request.POST.get('the_guest')
    #         response_data = {}

    #         guest = Guest(guest_name=guest_name, user=request.user)
    #         guest.save()

    #         response_data['result'] = 'Create post successful!'
    #         response_data['guestpk'] = guest.pk
    #         response_data['guest'] = guest.guest_name
    #         # response_data['created'] = guest.created.strftime('%B %d, %Y %I:%M %p')
    #         response_data['user'] = guest.user.username

    #         return HttpResponse(
    #             json.dumps(response_data),
    #             content_type="application/json"
    #         )
    #     else:
    #         return HttpResponse(
    #             json.dumps({"nothing to see": "this isn't happening"}),
    #             content_type="application/json"
    #         )


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
