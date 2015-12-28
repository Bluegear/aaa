from django.shortcuts import render

# Create your views here.
from oauth2_provider.decorators import protected_resource
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((AllowAny, ))
def hello(request):
    return Response({"message": "It's good to see you!"})


@api_view(['GET'])
@protected_resource()
@permission_classes((AllowAny, ))
@authentication_classes((OAuth2Authentication, ))
def get_secret(request):
    return Response({"message": "Congrat!"})