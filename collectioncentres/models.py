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

    def __str__(self):
        return self.location


class CollectionCentreStock(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of the stock',
    )
    centre = models.ForeignKey(
        CollectionCentre,
        on_delete=models.CASCADE,
    )
    item = models.CharField(
        max_length=30,
        help_text='Stock item',
    )
    quantity = models.IntegerField(
        help_text='Quantity in stock'
    )
    need_quantity = models.IntegerField(
        help_text='Quantity required'
    )
    unit = models.CharField(
        max_length=10,
        help_text='Unit of quantity'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user',
    )
