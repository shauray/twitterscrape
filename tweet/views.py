from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import twitter

# Create your views here.

def tweets(request):
	api = twitter.Api(consumer_key='vu0nooT8ZR9PL43KLxve7nIJk',
					  consumer_secret='0eEYyi2cusA51E7tbYKQty9rf8ogaWWSjF9a9OLH2BW2ux9tbH',
					  access_token_key='40794634-XziPIscShdkyoJFzpjdo5fvbOtIyvrrCnRmi0eDNs',
					  access_token_secret='dIJmABzBKSVg1Egsea7iVnsEKS1F4psoURqET962M8rxM')
	statuses = api.GetSearch(term="online education")

	return render_to_response('tweet/tweets.html', locals(), context_instance=RequestContext(request))