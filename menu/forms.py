from django.forms import ModelForm
from .models import Pizza, Topping, Sauce
from django.contrib.auth.models import User
from django import forms

class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['name']

class ToppingForm(forms.ModelForm):
    #name = forms.ChoiceField(choices=TOPPING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Topping
        fields = ['pizza']

class SauceForm(forms.ModelForm):
    #name = forms.ChoiceField(choices=TOPPING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Sauce
        fields = ['pizza']