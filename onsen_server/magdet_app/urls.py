from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import esp_input

urlpatterns = [
    path('', views.lock_confirm.as_view()),
    path('abe_hiroshi/', views.abe_hiroshi.as_view()),
    path('test/', esp_input),
]
