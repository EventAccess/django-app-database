from string import ascii_lowercase, digits

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

DISCORD_USERNAME_ALLOWED_CHARACTERS = set(ascii_lowercase + digits + "._")


def discord_username_validator(name: str) -> str | None:
    # TODO: Split up into multiple validators for form fields
    # https://docs.djangoproject.com/en/5.1/ref/forms/validation/
    #
    # https://support.discord.com/hc/en-us/articles/12620128861463-New-Usernames-Display-Names#h_01GXPQ8MBT04Y02QQFCPDHXHHG

    # Strip at-prefix (not part of the username)
    if name.startswith("@"):
        name = name.lstrip("@")

    # Usernames must be at least 2 characters and at most 32 characters long
    length = len(name)
    if length < 2 or length > 32:
        raise ValidationError(
            _("Discord username must be between 2 and 32 characters"),
            code="invalid",
        )

    # Usernames are case insensitive and forced lowercase
    name = name.lower()

    # Usernames cannot use any other special characters
    # besides underscore ( _ ) and period ( . )
    if not DISCORD_USERNAME_ALLOWED_CHARACTERS.issuperset(name):
        raise ValidationError(
            _("Discord username can only contain `%(characters)s`"),
            params={"characters": "".join(sorted(DISCORD_USERNAME_ALLOWED_CHARACTERS))},
            code="invalid",
        )

    # Usernames cannot use 2 consecutive period characters ( . )
    if ".." in name:
        raise ValidationError(
            _("Discord username cannot contain multiple consecutive periods (`..`)"),
            code="invalid",
        )

    return name
