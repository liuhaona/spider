# homework 1
import urllib.parse
import urllib.request
import re
import time
data=urllib.parse.urlencode({'wd':'刘'})
print(data)
ur1='http://www.baidu.com'
response=urllib.request.urlopen(ur1)
HTML=response.read().decode('utf8')
print(HTML)

#homework2
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]