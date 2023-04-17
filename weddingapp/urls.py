from . import views
from django.urls import path
from .views import create_event, EventList, GuestList

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('create_event/', create_event, name='create_event'),
    path('guestlist/', views.GuestList.as_view(), name='guestlist'),
]

# htmx_urlpatterns = [
#     path('add-guest/', views.add_guest, name='add-guest'),
# ]

# urlpatterns += htmx_urlpatterns
