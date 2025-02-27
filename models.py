from django.db import models
from .validators import discord_username_validator

# Create your models here.


class Attendant(models.Model):
    ticket_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    nfc_id = models.CharField(max_length=14, unique=True, null=False, blank=False)
    is_crew = models.BooleanField(default=False)
    _is_valid = models.BooleanField(name="is_valid", default=True)

    crewinfo = models.ForeignKey(
        "Crewmember", on_delete=models.CASCADE, default=None, null=True
    )

    @property
    def is_valid(self):
        # TODO: Validate daily ticket here
        return self._is_valid


class Crews(models.Model):
    name = models.CharField(max_length=32)


class Crewmember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    discord = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        validators=[discord_username_validator],
    )
    phone_number = models.CharField(max_length=15)
    crew = models.ForeignKey(Crews, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
