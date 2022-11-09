from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import PositiveIntegerField


def username_validator(username):
    for ch in username:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


POP = "Pop Music"
JAZZ = "Jazz Music"
RNB = "R&B Music"
ROCK = "Rock Music"
COUNTRY = "Country Music"
DANCE = "Dance Music"
HIP = "Hip Hop Music"
OTHER = "Other"

CHOICES = (
    (POP, POP),
    (JAZZ, JAZZ),
    (RNB, RNB),
    (ROCK, ROCK),
    (COUNTRY, COUNTRY),
    (DANCE, DANCE),
    (HIP, HIP),
    (OTHER, OTHER),
)


class Profile(models.Model):
    username = models.CharField(max_length=15, null=False, blank=False, validators=(MinLengthValidator(2),))
    email = models.EmailField(null=False, blank=False, )
    age = models.IntegerField(validators=(PositiveIntegerField,), null=True, blank=True)


class Album(models.Model):
    album_name = models.CharField(unique=True, max_length=30, null=False, blank=False, verbose_name='Album Name')
    artist_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Artist' )
    genre = models.CharField(max_length=30, null=False, blank=False, choices=CHOICES)
    description = models.TextField(null=True, blank=True, )
    image = models.URLField(null=False, blank=False, verbose_name='Image URL')
    price = models.FloatField(null=False, blank=False, validators=(PositiveIntegerField,))
