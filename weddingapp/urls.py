from . import views
from django.urls import path

urlpatterns = [
    path('', views.GuestList.as_view(), name='home'),
]
