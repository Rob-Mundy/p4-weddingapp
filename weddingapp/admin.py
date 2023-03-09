from django.contrib import admin
from .models import Event, Guest, Invitation
from django_summernote.admin import SummernoteInlineModelAdmin

# Register your models here.


@admin.register(Invitation)
class InvitationAdmin(SummernoteModelAdmin):

    summernote_fields = ('invitation_message')
