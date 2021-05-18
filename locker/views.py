from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . serializers import LockerSerializer
from . models import Locker
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : "/locker-list/",
        'Create' : "/locker-create/",
        'Detail View' : "/locker-detail/<int:id>",
        'Search' : "/locker-search/<str:city>"
    }

    return Response(api_urls)

@api_view(["GET"])
def getAllLockers(request):
    locker = Locker.objects.all()
    serializer = LockerSerializer(locker, many=True)
    return Response(serializer.data)
    