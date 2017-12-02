"""URLs for the ``cal`` app."""
from django.conf.urls import url

from . import views

urlpatterns = [

    # event views
    url(r'^event/create/$',
        views.EventCreateView.as_view(),
        name='calendar_event_create'),



    url(r'^(?P<year>\d+)/(?P<month>\d+)/$',
    views.MonthView.as_view(),
    name='cal_month'),

    url(r'^$',
        views.CalendariumRedirectView.as_view(),
        name='cal_current_month'),
]
