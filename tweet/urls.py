from django.conf.urls import patterns, url

from tweet import views

urlpatterns = patterns('',
	url(r'^$', views.tweets, name='index'),
	url(r'^tweets/', views.tweets, name='tweet_feed'),
	url(r'^tweets/cloud.json', views.cloud, name='cloud')
)	