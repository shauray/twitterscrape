from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^get-tweets-since/?get-tweets-since=(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', include('tweet.urls')), #where the form would have gone
    url(r'^tweet/', include('tweet.urls')), #page with timeframe form
    url(r'^tweets/', include('tweet.urls')), #page with tweets
)
	