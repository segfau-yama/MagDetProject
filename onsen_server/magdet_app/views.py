from django.shortcuts import render
from django.views.generic import ListView
from .models import availability
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


class lock_confirm(ListView):
    template_name = 'top.html'
    model = availability


@csrf_exempt
def esp_input(request):
    datas = json.loads(request.body)
    ava = availability.objects.get(pk=int(datas['room']))
    bool(datas['lock'])
    ava.lock = bool(datas['lock'])
    ava.save()
    """
    if ava.lock != update_lock:
        ava.lock = update_lock
        ava.save()
    """
    return HttpResponse("str(datas)")
