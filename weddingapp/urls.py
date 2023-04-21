from . import views
from django.urls import path
from .views import create_event, EventList, GuestList, GuestDetail

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('create_event/', create_event, name='create_event'),
    path('guestlist/', views.GuestList.as_view(), name='guestlist'),
    path('guestlist/<slug:slug>/', views.GuestDetail.as_view(), name='edit_guest'),
]
