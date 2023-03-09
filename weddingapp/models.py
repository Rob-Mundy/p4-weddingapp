from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    # confirmed_attendees = models.IntegerField()
    # declined_attendees = models.IntegerField()
    # unconfirmed_attendeed = models.IntegerField()


STATUS = ((0, "Draft"), (1, "Invited"))
IS_ATTENDING_CHOICES = [(False, 'No'), (True, 'Yes')]
DIETARY_REQUIREMENT_CHOICES = (
    (1, 'none'), (2, 'coeliac'), (3, 'food allergy'), (4, 'food intolerance'),
    (5, 'vegetarian'), (6, 'vegan'), (7, 'pescatarian'), (8, 'teetotal')
    )
PLUS_ONE_CHOICES = [(False, 'No'), (True, 'Yes')]


class Guest(models.Model):
    guest_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    email = models.EmailField()
    is_attending = models.BooleanField(
        "Attending?", default='', choices=IS_ATTENDING_CHOICES
    )
    message = models.TextField(blank=True)
    dietary_requirements = MultiSelectField(
        choices=DIETARY_REQUIREMENT_CHOICES
        )
    plus_one_attending = models.BooleanField(
        "Attending?", default='', choices=PLUS_ONE_CHOICES
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='guests'
        )
    invited = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-guest_name']

    def __str__(self):
        return self.guest_name
