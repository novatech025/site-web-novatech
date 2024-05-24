from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator

from event.models import EventModel
from django.db.models import Count


def index(request: WSGIRequest):
    context = {}

    latest_event_list = EventModel.objects.filter(published=True)
        
    paginator = Paginator(latest_event_list, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number if page_number is not None else 1)

    context["events"] = page_obj
    return render(request, "event/index.html", context)



def detail(request, event_id):
    target_event = EventModel.objects.get(id=event_id)

    context = {
        "event": target_event,
    }
    return render(request, "event/details.html", context)


