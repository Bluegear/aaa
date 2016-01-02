from django.db import IntegrityError
from mcweb.models import Merchant
from mcweb.serializers import MerchantSerializer
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class SignupView(APIView):
    """
    View for merchant signup.
    """
    permission_classes = (AllowAny,)
    renderer_classes = ([TemplateHTMLRenderer, ])

    def get(self, request):
        """
        Return signup form.
        """
        serializer = MerchantSerializer(Merchant())

        return Response(
                {'serializer': serializer,},
                template_name='mcweb/signup.html'
        )

    def post(self, request):
        """
        Return signup confirm page.
        """
        try:
            serializer = MerchantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                        None,
                        template_name='mcweb/signup_complete.html'
                )
            else:
                return Response(
                        {'serializer': serializer,},
                        template_name='mcweb/signup.html'
                )
        except IntegrityError:
            serializer._errors = {'display_name': [u'This name is already in use.']}
            return Response(
                    {
                        'serializer': serializer
                    },
                    template_name='mcweb/signup.html'
            )

