from django.db import models
from django.contrib.auth.models import User

class Camp(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of the camp',
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
        max_length=60,
        help_text='Location name',
    )

    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    capacity = models.IntegerField(
        help_text='The max capacity of the camp'        
    )
    number_of_people = models.IntegerField(
        default=0,
        help_text='The number of people currently in the camp'
    )

