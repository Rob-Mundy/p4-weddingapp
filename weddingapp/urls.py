from . import views
from django.urls import path
from .views import create_event, EventList, EventDetail, GuestList,
GuestDetail, delete_guest

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('create_event/', create_event, name='create_event'),
    path(
        'edit_event/<str:pk>/',
        views.EventDetail.as_view(),
        name='edit_event'
        ),
    path('guestlist/', views.GuestList.as_view(), name='guestlist'),
    path(
        'guestlist/<slug:slug>/',
        views.GuestDetail.as_view(),
        name='edit_guest'
        ),
    path('delete_guest/<str:pk>/', delete_guest, name="delete_guest"),
]
