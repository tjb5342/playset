from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse

import oauth2 as oauth
import urllib, rdio

def index(request):
    context = RequestContext(request)
    
    consumer = oauth.Consumer(key = "j7hyh4qg4fqcgrmdvdshdkqw", secret = "FdyJN4eZZ9")
    
    # Client is created as a worker attempting to execute a request to the Rdio API using consumer
    client = oauth.Client(consumer)
    
    # Make a 'get' request to the Rdio API for a particular album, store values in response
    response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method':'get','keys':'a184236'}))

    return HttpResponse("Welcome to Playset!")

# Create your views here.
