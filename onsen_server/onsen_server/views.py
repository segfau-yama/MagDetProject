from django.http import HttpResponse
from django.views.generic import TemplateView


class lock_confirm(TemplateView):
    template_name = 'top.html'
