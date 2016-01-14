from django.conf.urls import url
from mcweb.views.registrationview import RegistrationView
from .views.signupview import SignupView
from .views import indexview


urlpatterns = [
    url(r'^$', indexview.index, name='index'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
]