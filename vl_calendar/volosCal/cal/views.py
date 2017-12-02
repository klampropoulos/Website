from django.shortcuts import render
import calendar

from django.core.urlresolvers import reverse

from .models import Event
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    TemplateView,
    UpdateView,
)
from .models import EventCategory, Event
from django.utils.timezone import datetime, now, timedelta, utc
from .settings import SHIFT_WEEKSTART
from dateutil.relativedelta import relativedelta
# Create your views here.

class CategoryMixin(object):
    """Mixin to handle category filtering by category id."""
    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('category'):
            try:
                category_id = int(request.GET.get('category'))
            except ValueError:
                pass
            else:
                try:
                    self.category = EventCategory.objects.get(pk=category_id)
                except EventCategory.DoesNotExist:
                    pass
        return super(CategoryMixin, self).dispatch(request, *args, **kwargs)

    def get_category_context(self, **kwargs):
        context = {'categories': EventCategory.objects.all()}
        if hasattr(self, 'category'):
            context.update({'current_category': self.category})
        return context

class CalendariumRedirectView(RedirectView):
    """View to redirect to the current month view."""
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse('cal_month', kwargs={'year': now().year,
                                                 'month': now().month})

class MonthView(CategoryMixin, TemplateView):
    """docstring for MonthView."""
    """ MAIN VIEW """

    template_name = 'cal/cal_month.html'

    def dispatch(self, request, *args, **kwargs):
        self.month = int(kwargs.get('month'))
        self.year = int(kwargs.get('year'))
        if self.month not in range(1, 13):
            raise Http404
        if request.method == 'POST':
            if request.POST.get('next'):
                new_date = datetime(self.year, self.month, 1) + timedelta(
                    days=31)
                kwargs.update({'year': new_date.year, 'month': new_date.month})
                return HttpResponseRedirect(
                    reverse('cal_month', kwargs=kwargs))
            elif request.POST.get('previous'):
                new_date = datetime(self.year, self.month, 1) - timedelta(
                    days=1)
                kwargs.update({'year': new_date.year, 'month': new_date.month})
                return HttpResponseRedirect(
                    reverse('cal_month', kwargs=kwargs))
            elif request.POST.get('today'):
                kwargs.update({'year': now().year, 'month': now().month})
                return HttpResponseRedirect(
                    reverse('cal_month', kwargs=kwargs))

        return super(MonthView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        firstweekday = 0 + SHIFT_WEEKSTART
        while firstweekday < 0:
            firstweekday += 7
        while firstweekday > 6:
            firstweekday -= 7

        ctx = self.get_category_context()
        month = [[]]
        week = 0
        start = datetime(year=self.year, month=self.month, day=1, tzinfo=utc)
        end = datetime(
            year=self.year, month=self.month, day=1, tzinfo=utc
        ) + relativedelta(months=1)


        cal = calendar.Calendar()
        cal.setfirstweekday(firstweekday)
        for day in cal.itermonthdays(self.year, self.month):
            current = False
            if day:
                date = datetime(year=self.year, month=self.month, day=day,
                                tzinfo=utc)

                if date.date() == now().date():
                    current = True

            month[week].append((day, current))
            if len(month[week]) == 7:
                month.append([])
                week += 1
        calendar.setfirstweekday(firstweekday)
        weekdays = [(header) for header in calendar.weekheader(10).split()]
        ctx.update({'month': month, 'date': date, 'weekdays': weekdays})
        return ctx

class EventMixin(object):
    """Mixin to handle event-related functions."""
    model = Event
    fields = '__all__'

    #@method_decorator(permission_required('calendarium.add_event'))
    def dispatch(self, request, *args, **kwargs):
        return super(EventMixin, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('calendar_event_detail', kwargs={'pk': self.object.pk})

class EventUpdateView(EventMixin, UpdateView):
    """View to update information of an event."""
    pass


class EventCreateView(EventMixin, CreateView):
    """View to create an event."""
    pass


class EventDeleteView(EventMixin, DeleteView):
    """View to delete an event."""
    def get_success_url(self):
        return reverse('cal_current_month')
