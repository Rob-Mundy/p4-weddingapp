from django.shortcuts import render, redirect
from django.views import generic
from .models import Guest, Event, User
from django.core.mail import send_mail
from django.conf import settings
from .forms import createEventForm
from django.views.decorators.csrf import csrf_exempt


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
    template_name = 'guests.html'
    context_object_name = 'guests'

    def get_queryset(self):
        user = self.request.user
        # if user.is_authenticated:
        #     return Guest.objects.filter(user=user)
        return user.guests.all()


# def index(request):
#     form = createEventForm()
#     return render(request, 'index.html', {"form": form.as_p})

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


@csrf_exempt
def add_guest(request):
    name = request.POST.get('guestname')
    email = request.POST.get('guestemail')
    # event = request.POST.get('guestevent')
    guest = Guest.objects.create(guest_name=name)
    guestmail = Guest.objects.create(email=email)
    # guestevent = Guest.objects.create(event=event)
    
    # add the guest to the user's list
    request.user.guests.add(guest)
    # request.user.guests.add(guestmail) #moved to separate line

    # return template with all of the user's guests
    guests = request.user.guests.all()
    return render(request, 'partials/guestlist.html', {'guests': guests})
