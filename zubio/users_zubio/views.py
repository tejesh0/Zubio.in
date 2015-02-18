from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from elasticsearch import Elasticsearch
from django import forms
import pdb
es = Elasticsearch()


class SellerForm(forms.Form):
    prod_description = forms.CharField(
        label='product description', max_length=5000)
    months_used = forms.IntegerField()
    original_price = forms.IntegerField()
    selling_price = forms.IntegerField()
    quantity = forms.IntegerField()
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

            
            es.create(index="sell_form", doc_type="details", id=request.user.id, body=doc)

            return HttpResponse("Yo..!! Your item is attracting lot of buyers!!")
        return HttpResponse("Invalid details")
    else:   
        form = SellerForm()

    return render(request, 'seller_form.html', {'form': form})


def buyer_feed(request):

	#need to iterate over all product id's and append it to json and pass it in form_data
    # for
    # test = es.get(index="sell_form", doc_type="test-type", id=request.user.id)['_source']
    es.indices.refresh(index="sell_form")

    res = es.search(index="sell_form",body={"query": {"match_all": {}}})
    print res['hits']['total']
    form_data = []
    for i in res['hits']['hits']:
    	print "**************"
        print i
        form_data.append(i['_source'])

    return render(request, 'buyer_feed.html', {'form_data': form_data })
