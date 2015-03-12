from django.conf.urls import patterns, url

from tweet import views

urlpatterns = patterns('',
	#url(r'^$', views.tweets, name='index'),
	url(r'^tweets/', views.tweets, name='tweet_feed'),
	#url(r'^get-tweets-since/?get-tweets-since=(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', views.tweets, name='tweets'),
)