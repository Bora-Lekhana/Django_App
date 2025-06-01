
from django.contrib import admin
from .models import EventRegistration

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'eventname', 'date')
    search_fields = ('name', 'email', 'eventname')
