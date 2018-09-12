from django.db import models


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

    # Needs
    need_food = models.BooleanField(default=False)
    need_medicine = models.BooleanField(default=False)
    need_rescue = models.BooleanField(default=False)

    status = models.CharField(
        max_length=15,
        help_text='Status of request'
    )
