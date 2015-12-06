__author__ = 'darknight'

from django.conf.urls import url, patterns
from mail_list import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='index'),
        url(r'^code42day_registration$', views.code42day_registration, name='code42day_registration'),
)
