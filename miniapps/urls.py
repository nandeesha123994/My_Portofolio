from django.urls import path
from . import views

urlpatterns = [
    path('', views.miniapps_home, name='miniapps_home'),
]
