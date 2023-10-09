from django.urls import path
from . import views
urlpatterns=[
    path('',views.lobby),
    path('image_page', views.image_page),
]