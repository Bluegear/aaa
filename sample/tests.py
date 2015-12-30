from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.

class ViewsTestCase(TestCase):
    def test_hello(self):
        client = Client()
        response = client.get('sample/hello/')
        print(response.status_code)

