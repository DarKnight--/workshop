__author__ = 'darknight'

from django.conf.urls import url, patterns
from mail_list import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='index'),
)
