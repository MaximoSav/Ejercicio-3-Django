from django.urls import path
from .views import VistaHome

urlpatterns = [
    path('', VistaHome.as_view(), name='home'),
]