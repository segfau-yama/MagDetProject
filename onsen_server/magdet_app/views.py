from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import availability
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json


class lock_confirm(ListView):
    template_name = 'index.html'
    model = availability

    def post(self, request):
        datas = json.loads(request.body)
        ava = availability.objects.get(pk=int(datas['room']))
        bool(datas['lock'])
        ava.lock = bool(datas['lock'])
        ava.save()

        ctx = {'test': 1}
        return render(request, 'index.html', ctx)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(lock_confirm, self).dispatch(*args, **kwargs)


class abe_hiroshi(ListView):
    template_name = 'abe_hiroshi.html'
    model = availability


