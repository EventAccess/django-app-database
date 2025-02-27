from django.contrib import admin

# Register your models here.
from .models import Crewmember


class CrewmemberAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_number"]


admin.site.register(Crewmember, CrewmemberAdmin)
