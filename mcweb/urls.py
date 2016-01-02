from django.conf.urls import url
from .views.signupview import SignupView
from .views import indexview


urlpatterns = [
    url(r'^$', indexview.index, name='index'),
    url(r'^signup$', SignupView.as_view(), name='signup'),
]