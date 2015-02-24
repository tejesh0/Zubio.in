from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from elasticsearch import Elasticsearch
from django import forms
import pdb
import logging
es = Elasticsearch()
from datetime import datetime 


class SellerForm(forms.Form):
    prod_description = forms.CharField(
        label='product description', max_length=5000,required=False)
    months_used = forms.IntegerField(required=False)
    original_price = forms.IntegerField(required=False)
    selling_price = forms.IntegerField(required=False)
    quantity = forms.IntegerField(required=False)
    # is_active = forms.BooleanField(initial=True, hidden=True)
    # prod_image = forms.ImageField()
    # is_negotiable = forms.BooleanField(required=False,initial=True)

# Create your views here.


def seller_form(request):

    if request.method == "POST":
        # create a form instance and populate with data
        form = SellerForm(request.POST)
        # check whether form details are valid:
        if form.is_valid():
            # print request.POST
            # es.indices.refresh(index="sell_form")
            fields = ['prod_description','selling_price','months_used']
            doc= {}
            # pdb.set_trace()
            for field in fields:
                if request.POST[field]:
                    print request.POST[field]
                    doc[field] = request.POST[field]

            # tracer = logging.getLogger('elasticsearch.trace')
            # tracer.setLevel(logging.INFO)
            # tracer.addHandler(logging.FileHandler('/tmp/es_trace.log'))

            es.index(index="listing_page", doc_type="item", id=datetime.now(), body={'doc':{'prod':doc}})
            # i+=1

            return HttpResponse("Yo..!! Your item is attracting lot of buyers!!")
        return HttpResponse("Invalid details")
    else:   
        form = SellerForm()

    return render(request, 'seller_form.html', {'form': form})


def buyer_feed(request):

	#need to iterate over all product id's and append it to json and pass it in form_data
    # for
    # test = es.get(index="sell_form", doc_type="test-type", id=request.user.id)['_source']
    # es.indices.refresh(index="sell_form")

    res = es.search(index="listing_page",body={"query": {"match_all": {}}})
    print res['hits']['total']
    form_data = []
    for i in res['hits']['hits']:
    	print "**************"
        print i
        form_data.append(i['_source'])

    return render(request, 'index.html', {'form_data': form_data })
