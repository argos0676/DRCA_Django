from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, required=False)
    sender = forms.EmailField(required=True)
    tel = forms.CharField(max_length=15, required=False)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(max_length=140, required=True)
