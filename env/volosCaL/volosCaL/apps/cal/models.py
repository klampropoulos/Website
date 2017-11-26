from django.db import models

# Create your models here.


class Event(EventModelMixin):

    def get_pic_url(self,filename):
		return 'events/'+str(self.id)+'.jpg'

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=_('Created by'),
        related_name='events',
        blank=True, null=True,
    )

    start = models.DateTimeField(verbose_name=_('Start date'),)
    end = models.DateTimeField(verbose_name=_('End date'))
    creation_date = models.DateTimeField(verbose_name=_('Creation date'),auto_now_add=True)

    category = models.ForeignKey(
        'EventCategory',
        verbose_name=_('Category'),
        related_name='events',
        null=True, blank=True,
    )

    title = models.CharField(max_length=256,verbose_name=_('Title'),)
    image = FilerImageField(verbose_name=_('Image'),related_name='calendarium_event_images',null=True, blank=True)

    description = models.TextField(
        max_length=2048,
        verbose_name=_('Description'),
        blank=True,
    )

    image = models.ImageField(blank=True,upload_to=get_pic_url)

    def __str__(self):
		return self.title

	class Meta:
		verbose_name = _("Event")
		verbose_name_plural = _("Events")
