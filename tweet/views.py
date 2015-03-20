from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import csv, os, operator, twitter

# Create your views here.

def tweets(request):
	# API call for Tweets
	api = twitter.Api(consumer_key='vu0nooT8ZR9PL43KLxve7nIJk',
					  consumer_secret='0eEYyi2cusA51E7tbYKQty9rf8ogaWWSjF9a9OLH2BW2ux9tbH',
					  access_token_key='40794634-XziPIscShdkyoJFzpjdo5fvbOtIyvrrCnRmi0eDNs',
					  access_token_secret='dIJmABzBKSVg1Egsea7iVnsEKS1F4psoURqET962M8rxM')
	statuses = api.GetSearch(term="online education")
	# Gathering data about keywords in the tweets for D3
	words = {} 
	for status in statuses:
		text = status.text
		for split_word in text.split():
			split_word = split_word.encode("utf-8")
			# Filtering out unwanted words
			if (split_word[0] != '@' and split_word[:7] != 'http://' 
				and len(split_word) > 3 and len(split_word) < 20):
				if (split_word in words):
					words[split_word] += 1
				else:
					words[split_word] = 1
	# Adding to CSV File
	sorted_words = sorted(words.items(), key=operator.itemgetter(1))
	csv_data = [['word', 'value']]
	counter = 0
	#Gathering top 10 words
	for word in reversed(sorted_words):
		if (counter < 10):
			csv_data.append([word[0], word[1]])
		counter += 1
	filepath = os.path.dirname(os.path.abspath(__file__)) + "/static/word_data.csv"
	with open(filepath, 'wb') as csv_file:
			writer = csv.writer(csv_file, delimiter=',')
			writer.writerows(csv_data)
	return render_to_response('tweet/tweets.html', locals(), context_instance=RequestContext(request))