from django.shortcuts import render
from drinks.models.ourdrinks import ourDrinks


def index(request):
    ourdrinks = ourDrinks.objects.all()
    context = {
        'ourdrinks': ourdrinks,
    }
    return render(request, 'ourdrinks/index.html', context=context)
