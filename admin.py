from django.contrib import admin
from .models import Attendant, Crew

class AttendantAdmin(admin.ModelAdmin):
    list_display = ["ticket_id", "nfc_id", "is_crew", "is_valid"]


class CrewAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_number","discord"]


admin.site.register(Crew, CrewAdmin)
admin.site.register(Attendant, AttendantAdmin)


# Register your models here.
