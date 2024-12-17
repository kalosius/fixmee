from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    Model = Contact
    fields = ['name', 'phone', 'email', 'message']
