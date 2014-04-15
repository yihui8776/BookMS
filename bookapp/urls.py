# from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'book/create/$', 'bookapp.views.create_book'),
    url(r'book/list/$', 'bookapp.views.list_book'),
    url(r'book/edit/(?P<id>[^/]+)/$', 'bookapp.views.edit_book'),
    url(r'book/view/(?P<id>[^/]+)/$', 'bookapp.views.view_book'),
)
