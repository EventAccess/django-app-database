from django.contrib import admin

from .models import Attendant
from .models import Crewmember


class AttendantAdmin(admin.ModelAdmin):
    list_display = ["ticket_id", "nfc_id", "is_crew", "is_valid"]


admin.site.register(Attendant, AttendantAdmin)


class CrewmemberAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_number"]


admin.site.register(Crewmember, CrewmemberAdmin)
