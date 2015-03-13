from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(label="")
    title = forms.CharField()
    address = forms.CharField()
