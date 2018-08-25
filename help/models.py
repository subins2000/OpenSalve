from django.db import models


class Requests(models.Model):
    """Apart from directly specifying lat & lng, user
    can also input location name
    """
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    location = models.CharField(max_length=60)

    # Requestee info
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    request_for_others = models.BooleanField(default=False)

    # Needs
    need_food = models.BooleanField(default=False)
    need_medicine = models.BooleanField(default=False)
    need_rescue = models.BooleanField(default=False)
