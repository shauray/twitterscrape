from django.conf.urls import patterns, include, url
from django.contrib import admin

from tweet import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweets/', include('tweet.urls')),
)