from django.shortcuts import render
from django.views import generic
from .models import Guest


class GuestList(generic.ListView):
    model = Guest
    queryset = Guest.objects.order_by('-guest_name')
    template_name = 'index.html'
