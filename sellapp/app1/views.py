from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()


# Create your views here.
def seller_form(request):

	if request.method =="POST":
		es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

	else:
		HttpResponse("this is else block of post request")

	return HttpResponse("Yo..!! Your item is atteacting lot of buyers!!")