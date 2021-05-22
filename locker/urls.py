from django.urls import path
from . import views

urlpatterns =[
    path('', views.apiOverview, name="apiOverview"),
    path('locker-list/', views.getAllLockers, name="getAllLockers"),
    path('locker-detail/<int:pk>/', views.viewLocker, name="viewLocker"),
    path('locker-search/<str:searchQuery>/', views.searchLocker, name="searchLocker"),
    path('locker-create/', views.createLocker, name="createLocker"),
]