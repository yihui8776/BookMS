# from django.conf.urls.defaults import *
from models import *
from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    (r'book/create/$', create_book),
    (r'book/list/$', list_book ),
    (r'book/edit/(?P<id>[^/]+)/$', edit_book),
    (r'book/view/(?P<id>[^/]+)/$', view_book),
)