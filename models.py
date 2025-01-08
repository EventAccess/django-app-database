from django.db import models
from .validators import discord_username_validator

# Create your models here.


class Attendant(models.Model):
    ticket_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    nfc_id = models.BinaryField(max_length=7, unique=True, null=False, blank=False)
    is_crew = models.BooleanField(default=False)
    _is_valid = models.BooleanField(name="is_valid", default=True)

    @property
    def is_valid(self):
        # TODO: Validate daily ticket here
        return self._is_valid



class Crew(models.Model):
    attendant = models.ForeignKey(Attendant,on_delete=models.CASCADE) ##if we are deleting attandant object, delete crew aswell.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12)

    discord = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        validators=[discord_username_validator],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


