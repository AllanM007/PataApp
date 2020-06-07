from django.shortcuts import render
from .models import Pizza, Topping, Sauce
from .forms import PizzaForm, ToppingForm, SauceForm


def menu(request):
	form = ToppingForm()

	context = {
        'form':form,
    }
	return render(request, 'menu/menu.html', context)
