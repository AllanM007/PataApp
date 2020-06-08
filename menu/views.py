from django.shortcuts import render
from .models import Pizza
from .forms import PizzaForm


def menu(request):
	pizzas = Pizza.objects.all()
	
	context = {
        'pizzas':pizzas,
    }
	return render(request, 'menu/menu.html', context)

def pizza(request, pk):

	t_form = ToppingForm()
	s_form = SauceForm()

	pizza = Pizza.objects.get(pk = pk)
	
	context = {
        'pizza':pizza,
        't_form':t_form,
        's_form':s_form,
    }

	return render(request, 'menu/pizza.html', context)