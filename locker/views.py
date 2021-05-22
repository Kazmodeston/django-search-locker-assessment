from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

from . serializers import LockerSerializer
from . models import Locker
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : "/locker-list/",
        'Create' : "/locker-create/",
        'Detail View' : "/locker-detail/<int:id>",
        'Search' : "/locker-search/<str:searchQuery>"
    }

    return Response(api_urls)


@api_view(["GET"])
def getAllLockers(request):
    lockers = Locker.objects.all()
    serializer = LockerSerializer(lockers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def viewLocker(request, pk):
    locker = Locker.objects.get(id=pk)
    serializer = LockerSerializer(locker, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def searchLocker(request, searchQuery):
    # city = request.data['city']
    lockers = Locker.objects.filter(Q(city__icontains=searchQuery) | Q(state__icontains=searchQuery) | Q(featured__icontains=searchQuery))
    serializer = LockerSerializer(lockers, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def createLocker(request):
    serializer = LockerSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)