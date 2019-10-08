from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Your name")
    surname = forms.CharField(label="Your surname")