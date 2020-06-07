from django.shortcuts import render
from .models import Pizza, Topping, Sauce
from .forms import PizzaForm, ToppingForm, SauceForm


def menu(request):
	pizzas = Pizza.objects.all()
	
	form = ToppingForm()

	context = {
        'form':form,
        'pizzas':pizzas,
    }
	return render(request, 'menu/menu.html', context)
