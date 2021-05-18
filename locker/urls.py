from django.urls import path
from . import views

urlpatterns =[
    path('', views.apiOverview, name="apiOverview"),
    path('locker-list', views.getAllLockers, name="getAllLockers")
]