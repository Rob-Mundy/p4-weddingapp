from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Guest, Event, User
from django.conf import settings
from .forms import createEventForm, editEventForm, addGuestForm, editGuestForm
from slugify import slugify
from django.core.exceptions import ValidationError


# class EventList(generic.ListView):

#     def get(self, request, *args, **kwargs):
#         user = self.request.user
#         queryset = Event.objects.filter(user=user)
#         context_object_name = 'events'
#         # form = addGuestForm(request.POST or None)

#         return render(
#             request,
#             "index.html",
#             {
#                 "events": queryset,
#                 "user": user
#             }
#         )

class EventList(generic.ListView):
    model = Event
    template_name = 'index.html'
    context_object_name = 'events'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Event.objects.filter(user=user)
            # return Event.objects.all()[0]


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


def delete_guest(request, pk):
    queryset = Guest.objects.get(id=pk)
    name = Guest.guest_name
    if request.method == 'POST':
        queryset.delete()
        return redirect("guestlist")
    return render(request, 'delete_guest.html')


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


# def edit_event(self, request, *args, **kwargs):
#     user = self.request.user
#     queryset = Event.objects.filter(user=user)
#     instance = get_object_or_404(queryset, pk=guest.id)
#     form = editEventForm(data=request.POST, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect("/")

#     return render(
#         request,
#         "edit_event.html",
#         {
#             "instance": instance,
#             "form": form
#         }
#     )

# class EventDetail(generic.UpdateView):

#     def get(self, request, pk, *args, **kwargs):
#         user = self.request.user
#         queryset = Event.objects.filter(user=user)
#         instance = get_object_or_404(queryset, pk=pk)
#         form = editEventForm(request.POST or None, instance=instance)

#         return render(
#             request,
#             "edit_event.html",
#             {
#                 "instance": instance,
#                 "form": form
#             }
#         )

#     def post(self, request, pk, *args, **kwargs):
#         user = self.request.user
#         queryset = Event.objects.filter(user=user)
#         instance = get_object_or_404(queryset, pk=pk)
#         form = editEventForm(data=request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect("/")

#         return render(
#             request,
#             "edit_event.html",
#             {
#                 "instance": instance,
#                 "form": form
#             }
#         )
