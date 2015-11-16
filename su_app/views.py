from django.shortcuts import render

# Create your views here.

from rest_framework import (
	authentication,
	permissions,
	viewsets,
	status
)
from rest_framework.response import Response

from models import StatusUpdate
from serializers import StatusUpdateSerializer
from pagination import CustomPagination

class DefaultsMixin(object):
    paginate_by         = 25
    paginate_by_param   = 'page_size'
    max_paginate_by     = 100
    pagination_class	= CustomPagination


class StatusUpdateViewSet(DefaultsMixin, viewsets.ModelViewSet):
	""" API endpoint for listing and creating status updates """

	queryset 			= StatusUpdate.objects.all()
	serializer_class 	= StatusUpdateSerializer

from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    from yookosusers import YookosUser
    user = YookosUser()
    res = user.get_upm('jomski2009')
    if res:
        response = res['username'] +'</br>' +res['firstname'] +'</br>' + res['lastname']
    else:
        response = 'Could not get the profile'
    return HttpResponse(response)
