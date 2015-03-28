from django.shortcuts import render,render_to_response
from django import forms
# import the logging library
import logging
from elasticsearch import Elasticsearch
import json


es = Elasticsearch()
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gym.models import Document
from gym.forms import DocumentForm

def gym_listing_form(request):
    """
        Form available to subadmins to list a new gym after verification
        of detailed escription of gym.

    """
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponse("lol")
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def login(request):
    return render_to_response(
            'login.html',
            {}
    )

def index(request):
    return render_to_response(
            'index.html',
            {}
    )

def gym_profile(request):
    return render_to_response(

            'gym-profile.html',
            {}
    )

def search_listings(request):
    """
    assuming location will be provided in request variable from urlresolvers



    """

    #query postgresql database given location
    #build a view as an abstract layer in models.py to get gyms based on location
    #push each result to gyms dictionary
    


    gyms = {}

    return render_to_response('listings.html', {gyms:gyms})

def api(request):
    if request.method == 'GET':
        q = request.GET.get('q',None)
        logger.error('Something went wrong!')
        if not q:
            q = '*'
        else:
            q = q + '*'
    else:
        return HttpResponse("Learn to request !!~~!!")
    contents = []
    try:
        res = es.search(index='zubio',doc_type='locations', q=q)['hits']['hits']
        for result in res:
            res_get =  result.get('_source', "")

            contents.append(res_get)

        return HttpResponse(json.dumps({"contents":contents}), content_type="application/json")
    except:
        pass
    return HttpResponse("rope in the wings")

