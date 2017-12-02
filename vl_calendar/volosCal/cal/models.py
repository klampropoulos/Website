from django.db import models

#my imports
from filer.fields.image import FilerImageField
from location_field.models.plain import PlainLocationField
from colorfield.fields import ColorField
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


# The event model
class Event(object):
    """docstring for Event."""

    title = models.CharField(max_length=256, verbose_name=('Title'))

    created_by = models.ForeignKey(
        User,
        verbose_name=('Created by'),
        editable = False,
        blank=True, null=True,
    )

    exact_location = models.CharField(
        max_length=256,
        verbose_name=('exact_location'),
        default="",
    )

    city= "Volos"

    location = PlainLocationField(based_fields=['city'+'locat'], zoom=5) # for the map

    category = models.ForeignKey(
        'EventCategory',
        verbose_name=('Category'),
        related_name='events',
        null=True, blank=True,
    )

    def get_pic_url(self, filename):
        return '/cal/'+str(self.id)+'.jpg'

    image = models.ImageField(blank=True,upload_to=get_pic_url)
    start_date = models.DateTimeField(verbose_name=("Start Date"))
    end_date = models.DateTimeField(verbose_name=("End Date"))

    description = models.CharField(max_length=256, verbose_name=('Description'))


    def __str__(self):
        return self.title


class EventCategory(models.Model):
    name = models.CharField(max_length=256,verbose_name=('Name'))

    color = ColorField(default='#FF0000', verbose_name=('Color'))

    def __str__(self):
        return self.name
