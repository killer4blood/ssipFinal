from django.shortcuts import render
from drinks.models.topping import Topping


def index(request):
    toppings = Topping.objects.all()
    data = {
        'toppings': toppings,
    }
    return render(request, 'topping/index.html', data)

