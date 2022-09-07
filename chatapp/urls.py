from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('base', views.base),
    path('sent_msg/<str:pk>/', views.sendMessage, name="sent_msg"),
    path('friend/<str:pk>/', views.details,name="detail"),
]

