from django.db import models

from accounts.models import Users


class Requests(models.Model):
    """Apart from directly specifying lat & lng, user
    can also input location name
    """
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of request',
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

    # Requestee info
    name = models.CharField(
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
        max_length=40,
        help_text='Where this request call was obtained from',
    )

    # Needs
    need_food = models.BooleanField(default=False)
    need_medicine = models.BooleanField(default=False)
    need_rescue = models.BooleanField(default=False)

    status = models.CharField(
        max_length=15,
        help_text='Status of request'
    )


class Comments(models.Model):
    """Comments in requests
    """

    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of comment',
    )

    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        db_column='user',
    )
