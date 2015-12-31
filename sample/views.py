from django.core.urlresolvers import reverse
from oauth2_provider.decorators import protected_resource
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import sample

@api_view(['GET'])
@permission_classes((AllowAny, ))
def index(request):
    """<h3>APIs index</h3>
    """
    apis = []
    for url in sample.urls.urlpatterns:
        apis.append("http://%s%s" % (request.META['HTTP_HOST'], reverse(url.callback)))

    return Response({"apis": apis})


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


@permission_classes((AllowAny, ))
class SampleView(APIView):
    """
    Sample of a class based view.
    """

    def get(self, request):
        """

        :param request:
        :return: Static json
        """
        return Response({"message": "This is a classy based view."})
