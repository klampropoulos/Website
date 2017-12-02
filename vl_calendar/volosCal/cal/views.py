from django.shortcuts import render


from django.views.generic import CreateView, DetailView, ListView , UpdateView
from el_pagination.views import AjaxListView
from .models import Event
from django.contrib.auth.models import User
# Create your views here.

class MonthView(object):
    """docstring for MonthView."""
    def __init__(self, arg):
        super(MonthView, self).__init__()
        self.arg = arg
