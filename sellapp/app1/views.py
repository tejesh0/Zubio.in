from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from elasticsearch import Elasticsearch
from django import forms

es = Elasticsearch()

class SellerForm(forms.Form):
	prod_description = forms.CharField(label='Looking for buyers interested in..',max_length=5000)


# Create your views here.
def seller_form(request):

	if request.method =="POST":
		#create a form instance and populate with data
		form = SellerForm(request.POST)
		#check whether form details are valid:
		if form.is_valid():
			print "yooo!!!!!!!!!!!!"
			print request.POST['prod_description']
			es.index(index="my-index", doc_type="test-type", id=42, body={"prod_description":request.POST['prod_description'],"any": "data", "timestamp": datetime.now()})
			HttpResponse("Yo..!! Your item is attracting lot of buyers!!")
	else:
		form = SellerForm()

	return render(request, 'seller_form.html', {'form':form})


def buyer_feed(request):

	test = es.get(index="my-index", doc_type="test-type", id=42)['_source']
	
	return render(request, 'buyer_feed.html', {'form_data':test})