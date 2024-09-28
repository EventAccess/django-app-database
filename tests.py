from django.forms import ValidationError
import pytest

from .validators import discord_username_validator


@pytest.mark.parametrize(
    "name",
    [
        "@oddstr13",
        "ab",
        "user.name",
        "user_name",
    ],
)
def test_discord_names(name):
    discord_username_validator(name)


@pytest.mark.parametrize(
    "name",
    [
        "a",
        "@a",
        "123456789012345678901234567890123",
        "Ægis",
        "botty..mc.botface",
        "user-name",
        "$$$",
    ],
)
def test_discord_invalid_names(name):
    with pytest.raises(ValidationError):
        discord_username_validator(name)
