from django.shortcuts import render_to_response, HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gym.models import FitnessListing, FitnessListingForm
# from gym.forms import DocumentForm
from django.shortcuts import render, render_to_response
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import the logging library
import logging
logger = logging.getLogger(__name__)
from elasticsearch import Elasticsearch
import json


es = Elasticsearch()
# Get an instance of a logger
logger = logging.getLogger(__name__)


def gym_listing_form(request):
    """
        Form available to subadmins to list a new gym after verification
        of detailed escription of gym.

    """

    # Handle file upload
    if request.method == 'POST':

        form = FitnessListingForm(request.POST, request.FILES)
        print "pst"
        print form
        logging.warn(form)
        if form.is_valid():
            g = FitnessListing(Gallery=request.FILES['Gallery'])

            address, title, description = request.POST['Address'], request.POST[
                'Name_Of_The_Fitness_Center'], request.POST['Description']

            store = {"description": description,
                     "title": title, "address": address}
            es.create(index='gym_profile', doc_type='listings', body=store)


            fulltext = es.search(
                index='gym_profile', doc_type='listings', q="*")

            # Redirect to the document list after POST
            return HttpResponse(json.dumps({'fulltext': fulltext}))
    else:
        form = FitnessListingForm()  # A empty, unbound form

    # Load documents for the list page
    documents = FitnessListing.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
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


def upload_form(request):
    return render_to_response(

        'upload-form.html',
        {}
    )


def trainer_profile(request):
    return render_to_response(

        'trainer-profile.html',
        {}
    )


def search_listings(request):
    """
    assuming location will be provided in request variable from urlresolvers



    """
    logger.warning("get request tj {}".format(request.GET.get('query')))
    # print http.request
    if request.method == 'GET':
        logger.warning("get request tj {}".format(request.GET.get('query')))
        q = request.GET.get('query', None)
        l = request.GET.get('locality', None)

        fulltext = es.search(
            index='gym_profile', doc_type='listings', q=q + " " + l)



        # Redirect to the document list after POST
        # return render_to_response('listings.html', {'results':fulltext})
        return HttpResponse(json.dumps({'fulltext': fulltext}))

    return render_to_response('listings.html', {gyms: gyms})


def api(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)
        logger.error('Something went wrong!')
        if not q:
            q = '*'
        else:
            q = q + '*'
    else:
        return HttpResponse("Learn to request !!~~!!")
    contents = []
    try:
        res = es.search(index='zubio', doc_type='locations', q=q)[
            'hits']['hits']
        for result in res:
            res_get = result.get('_source', "")

            contents.append(res_get)

        return HttpResponse(json.dumps({"contents": contents}), content_type="application/json")
    except:
        pass
    return HttpResponse("rope in the wings")


def myfunction():
    logger.debug("this is a debug message!")
 
def myotherfunction():
    logger.error("this is an error message!!")