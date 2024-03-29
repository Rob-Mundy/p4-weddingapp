from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=False,
        default=int(1), related_name='events'
        )

    def __str__(self):
        return self.event_name


STATUS = ((0, "Draft"), (1, "Invited"))
IS_ATTENDING_CHOICES = [(False, 'No'), (True, 'Yes')]
DIETARY_REQUIREMENT_CHOICES = (
    (1, 'none'), (2, 'coeliac'), (3, 'food allergy'), (4, 'food intolerance'),
    (5, 'vegetarian'), (6, 'vegan'), (7, 'pescatarian'), (8, 'teetotal')
    )
PLUS_ONE_CHOICES = [(False, 'No'), (True, 'Yes')]


class Guest(models.Model):
    guest_name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    email = models.EmailField()
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True,
        related_name='guests'
        )
    attending = models.BooleanField(
        "Attending?", default='', choices=IS_ATTENDING_CHOICES, null=True
    )
    plus_one_attending = models.BooleanField(
        "Plus one?", default=True, choices=PLUS_ONE_CHOICES
    )
    dietary_requirements = MultiSelectField(
        choices=DIETARY_REQUIREMENT_CHOICES
        )
    invited = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False,
        default=int(1), related_name='guests'
        )

    class Meta:
        ordering = ['guest_name']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'guest_name'],
                name='unique guest for each user'
                )
        ]

    def __str__(self):
        return self.guest_name


class Invitation(models.Model):
    invitation_name = models.CharField(max_length=200, unique=True)
    invitation_image = CloudinaryField('image', default='placeholder')
    invitation_message = models.TextField()
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, blank=False, null=False,
        default=int(1)
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False,
        default=int(1), related_name='invitation'
        )
