from django.db import models
from django.contrib.auth.models import User


class CollectionCentre(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of the collection centre',
    )
    lat = models.CharField(
        max_length=20,
        help_text='Latitude',
    )
    lng = models.CharField(
        max_length=20,
        help_text='Longitude',
    )
    location = models.CharField(
        max_length=200,
        help_text='Location name',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user',
    )
