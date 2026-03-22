from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='learning_home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
