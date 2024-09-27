from django.db import models
from .validators import discord_username_validator

# Create your models here.


class Attendant(models.Model):
    ticket_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    nfc_id = models.BinaryField(max_length=7, unique=True, null=False, blank=False)
    discord = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        validators=[discord_username_validator],
    )
    is_crew = models.BooleanField(default=False)
    _is_valid = models.BooleanField(name="is_valid", default=True)

    @property
    def is_valid(self):
        # TODO: Validate daily ticket here
        return self._is_valid
