from django.core.urlresolvers import reverse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
import oauthext


@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def index(request):
    """<h3>APIs index</h3>
    """
    apis = []
    for url in oauthext.urls.urlpatterns:
        apis.append("http://%s%s" % (request.META['HTTP_HOST'], reverse(url.callback)))

    return Response({"apis": apis})


# TODO: Change to appropriate method and permission e.g. POST with Authorization header.
@api_view(['GET'])
@permission_classes((AllowAny, ))
def introspect(request):
    """<h3>Introspect</h3>
    :param request:access_token, scope
    """

    # TODO: Validate Access Token and its scope.

    # TODO: Fetch additional information relate to this token.

    # TODO: API Docs about response.
    return Response({"active": True, "tmn_id": "abc", "mc_int_wallet_id": "1234"})
