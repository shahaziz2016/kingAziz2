from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from patiant.models import Ehr1
	
urlpatterns = [url(r'^$', ListView.as_view(queryset = Ehr1.objects.all().order_by("-appointmentDate")[:25],template_name="patiant/patiant.html")),]