from django.db import models
from django import forms

# Create your models here.
# (choices=[(x, x) for x in range(1, 32)])

class Document(models.Model):
	title = models.CharField(max_length=50, default="please fill")
	address = models.CharField(max_length=500,default="please fill")
	description = models.CharField(max_length=500, default="Description")
	# offerings = forms.ChoiceField(choices=[('spa','spa'),('gym','gym')])
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    
# class GymForm(models.Model):
# 	title = models.CharField(max_length=50,default="Gym")
