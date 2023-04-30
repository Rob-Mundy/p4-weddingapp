from django.contrib import admin
from .models import Event, Guest
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Event)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'slug', 'invited', 'attending', 'plus_one_attending')
    search_fields = ['guest_name', 'invited']
    prepopulated_fields = {'slug': ('user', 'guest_name',)}
    # slugfield prepopulated with user + guest_name so that 
    # slug is unique for user as guest_name is not unqique
    # site-wide
    list_filter = ('guest_name', 'attending')
