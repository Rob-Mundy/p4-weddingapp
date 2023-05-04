from . import views
from django.urls import path
from .views import create_event, EventList, EventDetail, GuestList
from .views import GuestDetail, delete_guest

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('create_event/', create_event, name='create_event'),
    path(
        'edit_event/<str:pk>/',
        views.EventDetail.as_view(),
        name='edit_event'
        ),
    path('guest_list/', views.GuestList.as_view(), name='guest_list'),
    path(
        'guest_list/<slug:slug>/',
        views.GuestDetail.as_view(),
        name='edit_guest'
        ),
    path('delete_guest/<str:pk>/', delete_guest, name="delete_guest"),
]
