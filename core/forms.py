from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=40, required=False)
    sender = forms.EmailField(label='Email', required=True)
    tel = forms.CharField(label='Telefone', max_length=15, required=False)
    subject = forms.CharField(label='Assunto', max_length=100, required=True)
    message = forms.CharField(label='Messagem', widget=forms.Textarea, max_length=200, required=True)
    #cc_myself = forms.BooleanField(required=False)