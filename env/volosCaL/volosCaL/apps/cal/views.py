from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView , UpdateView
from el_pagination.views import AjaxListView
from .models import Event
from django.contrib.auth.models import User
# Create your views here.

class EventListView(AjaxListView):
	context_object_name = 'event_list'
	template_name = 'events/event_list.html'
	page_template = ('events/event_list_page.html')

	def get_queryset(self):
		return Event.objects.all()

class EventDetailView(DetailView):
	model = Event

	def get_object(self):
		return Event.objects.get(pk=self.kwargs.get("event_id"))
