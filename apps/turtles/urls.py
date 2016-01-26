from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
  url(r'^ninja/$', views.index, name='index'),
  url(r'^ninja/(?P<color>\D+)/$', views.color)
)
