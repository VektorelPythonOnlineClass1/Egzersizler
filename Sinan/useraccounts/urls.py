# useraccounts/urls.py
from django.urls import path
from django.conf.urls import url
from . import views as useraccounts_views



urlpatterns = [
    url(r'^signup/$', useraccounts_views.signup, name='signup'),
]