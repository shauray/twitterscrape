from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('tweet.urls'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweets/', include('tweet.urls')), #page with tweets
	url(r'^tweets/population.csv', include('tweet.urls'))
)
	