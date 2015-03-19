from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import os
import twitter

# Create your views here.

def tweets(request):
	api = twitter.Api(consumer_key='vu0nooT8ZR9PL43KLxve7nIJk',
					  consumer_secret='0eEYyi2cusA51E7tbYKQty9rf8ogaWWSjF9a9OLH2BW2ux9tbH',
					  access_token_key='40794634-XziPIscShdkyoJFzpjdo5fvbOtIyvrrCnRmi0eDNs',
					  access_token_secret='dIJmABzBKSVg1Egsea7iVnsEKS1F4psoURqET962M8rxM')
	statuses = api.GetSearch(term="online education")

	words = {}
	for status in statuses:
		text = status.text
		for split_word in text.split():
			split_word = split_word.encode("utf-8")
			print split_word
			if (split_word in words):
				words[split_word] += 1
			else:
				words[split_word] = 1
	formatted_words = []
	#for word in words:
	#	formatted_words.append(word + ": " + words[word])

	filepath = os.path.dirname(os.path.abspath(__file__)) + "/templates/tweet/cloud.json"
	#with open(filepath, "a") as jsonFile:
		#import string
		#for word in words:	
		#	for c in string.punctuation:
		#		word = word.replace(c, "")
		#	size = words[word] * 100
			#jsonFile.write('{"name": "' + str(word) + '", "size": ' + str(size) + '}, \n')
		#jsonFile.write("]\n}\n]\n}\n]\n}")
	return render_to_response('tweet/tweets.html', locals(), context_instance=RequestContext(request))

def cloud(request):
	return open(os.path.dirname(os.path.abspath(__file__)) + "/templates/tweet/cloud.json")
def population(request):
	return open(os.path.dirname(os.path.abspath(__file__)) + "/templates/tweet/population.csv")