from django.shortcuts import render,render_to_response
from django import forms

# Create your views here.


# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gym.models import Document
from gym.forms import DocumentForm

def list(request):
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
        'gym-profile.html',
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
            'gymProfile.html',
            {}
    )