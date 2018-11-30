from django import forms
from .models import Store

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label="Last name", max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email address", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)


class SearchStoresForm(forms.Form):
    ITEM_TYPE_CHOICES = (('clothing', 'Clothing'),
                         ('hat', 'Hat'),
                         ('kitchen', 'Kitchen'),
                         ('electronics', 'Electronics'),
                         ('household', 'Household'),
                         ('other', 'Other'),
                         )

    item_name = forms.CharField(max_length=100, required=False)
    item_category = forms.ChoiceField(choices=ITEM_TYPE_CHOICES, widget=forms.RadioSelect, required=False)
    store = forms.ModelChoiceField(queryset=Store.objects.all(), widget=forms.RadioSelect, required=False)

