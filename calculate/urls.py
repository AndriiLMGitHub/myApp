from django.urls import path
from . import views
from django.views.generic import ListView
from calculate.models import Calculates

urlpatterns = [
    path('', ListView.as_view(queryset = Calculates.objects.all().order_by("-date")[:10] ,
    template_name = "calculate/calculate.html" ),)
]
