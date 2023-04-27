from django.contrib import admin
from .models import Event, Guest
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Event)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'slug', 'invited', 'attending', 'plus_one_attending')
    search_fields = ['guest_name', 'invited']
    prepopulated_fields = {'slug': ('user', 'guest_name',)}
    list_filter = ('guest_name', 'attending')


# @admin.register(Invitation)
# class InvitationAdmin(SummernoteModelAdmin):
#     summernote_fields = ('invitation_message')
#     list_display = ('invitation_name', 'user')
