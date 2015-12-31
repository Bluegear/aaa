from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^secret/', views.get_secret),
    url(r'^classy/', views.SampleView.as_view()),
]