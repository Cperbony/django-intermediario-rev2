from django import forms
from .models import STATES_CHOICES


class AddressForm(forms.Form):
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_complement = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        choices=STATES_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
