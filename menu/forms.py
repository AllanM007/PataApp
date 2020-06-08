from django.forms import ModelForm
from .models import Pizza
from django.contrib.auth.models import User
from django import forms

TOPPING_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

SAUCE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class PizzaForm(forms.ModelForm):
	#name = forms.ChoiceField(choices=TOPPING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Pizza
        fields = ['name']