from django.db import models

from django.contrib.auth.models import User


class Requests(models.Model):
    """Apart from directly specifying lat & lng, user
    can also input location name
    """
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of request',
    )
    lat = models.CharField(
        blank=True,
        max_length=20,
        help_text='Latitude',
    )
    lng = models.CharField(
        blank=True,
        max_length=20,
        help_text='Longitude',
    )
    location = models.CharField(
        blank=True,
        max_length=60,
        help_text='Location name',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Requestee info
    name = models.CharField(
        blank=True,
        max_length=50,
        help_text='Name of requestee',
    )
    phone = models.CharField(
        max_length=20,
        help_text='Phone of requestee',
    )

    request_for_others = models.BooleanField(
        default=False,
        help_text='Whether this request is not made for yourself',
    )
    number_of_people_with_you = models.IntegerField(
        default=0,
        help_text='The number of people stranded with you'
    )
    source = models.CharField(
        blank=True,
        max_length=40,
        help_text='Where this request call was obtained from',
    )

    # Needs
    need_food_water = models.BooleanField(default=False)
    need_first_aid = models.BooleanField(default=False)
    need_rescue = models.BooleanField(default=False)
    need_transport = models.BooleanField(default=False)
    need_medical = models.BooleanField(default=False)

    status = models.CharField(
        blank=True,
        max_length=50,
        help_text='Status of request'
    )

    desc = models.CharField(
        blank=True,
        max_length=200,
        help_text='Further description'
    )

    def __str__(self):
        return self.name


class Comments(models.Model):
    """Comments in requests
    """

    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of comment',
    )

    request = models.ForeignKey(
        Requests,
        on_delete=models.CASCADE,
        db_column='request',
        help_text='The request to which this comment is made',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user',
    )

    comment = models.CharField(
        max_length=1000,
        help_text='Comment text'
    )

    created_at = models.DateTimeField(auto_now_add=True)
