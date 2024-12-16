from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    form = Contact
    fields = ['name', 'phone', 'email', 'message']
