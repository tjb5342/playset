from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

import oauth2 as oauth
import urllib, rdio

def index(request):
    context = RequestContext(request)
    
    # Initialize the an Rdio Api whisperer
    bigR = rdio.Api("j7hyh4qg4fqcgrmdvdshdkqw","FdyJN4eZZ9")
    user = bigR.find_user(email='tjb5342@gmail.com')
    
    # Identify consumer by the key,secret associated with Playset API key 
    consumer = oauth.Consumer(key = "j7hyh4qg4fqcgrmdvdshdkqw", secret = "FdyJN4eZZ9")
    
    # Client is created as a worker attempting to execute a request to the Rdio API using consumer
    client = oauth.Client(consumer)
    
    # Make a 'get' request to the Rdio API for a particular album, store values in response
    response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method':'get','keys':'a184236'}))
        
    # Get a playback token
    playback_token = bigR.get_playback_token('localhost1')
    
    context_dict = {'rdio_user': user,
                    'playback_token': playback_token,}
    
    return render_to_response('playset/index.html', context_dict, context)

