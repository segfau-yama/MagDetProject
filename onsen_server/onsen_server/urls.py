from django.contrib import admin
from django.urls import path, include
from .views import lock_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('magdet_app.urls')),
]
