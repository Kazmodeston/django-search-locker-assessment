from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.

def apiOverview(request):
    api_urls = {
        'List' : "/locker-list/",
        'Create' : "/locker-create/",
        'Detail View' : "/locker-detail/<int:id>",
        'Search' : "/locker-search/<str:city>",
    }

    return Response(api_urls)