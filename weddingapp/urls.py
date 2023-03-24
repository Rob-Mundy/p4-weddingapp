from . import views
from django.urls import path
from .views import create_event

urlpatterns = [
    path('', views.GuestList.as_view(), name='home'),
    path('create_event/', create_event, name='create_event'),
]
