from django.contrib import admin
from .models import Event, Guest, Invitation
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Event)

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'invited', 'attending', 'plus_one_attending')
    search_fields = ['guest_name', 'invited']
    prepopulated_fields = {'slug': ('guest_name',)}
    list_filter = ('guest_name', 'attending')


@admin.register(Invitation)
class InvitationAdmin(SummernoteModelAdmin):
    summernote_fields = ('invitation_message')
    list_display = ('invitation_name', 'event')
