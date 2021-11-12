from django import forms
from django.db.models import fields
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        #exclude = ["owner"]
        fields = ('title', 'price', 'text', 'owner')