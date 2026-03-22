from django.urls import path
from . import views


urlpatterns=[
  path('',views.contact, name='contact'),
  path('toggle-mode/', views.toggle_recruiter_mode, name='toggle_mode'),
]