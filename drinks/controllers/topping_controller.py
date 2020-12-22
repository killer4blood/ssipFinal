from django.shortcuts import render
from drinks.models.topping import Topping

def index(request):
    topping = Topping.objects.all()
    context = {
        'topping': topping,
    }
    return render(request, 'topping/index.html', context=context)
