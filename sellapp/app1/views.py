from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from elasticsearch import Elasticsearch
from django import forms

es = Elasticsearch()


# Create your views here.
def seller_form(request):

	if request.method =="POST":
		#create a form instance and populate with data
		form = NameForm(request.POST)
		#check whether form details are valid:
		if form.is_valid():
			es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
			HttpResponse("Yo..!! Your item is attracting lot of buyers!!")
	else:
		form = SellerForm()

	return render(request, 'seller_form.html', {'form':form})


class SellerForm(forms.Form):
	prod_description = forms.TextField(label='Looking for buyers interested in..',max_length=5000)
