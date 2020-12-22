from django.shortcuts import render
from drinks.models.sugar import Sugar


def index(request):
    sugar = Sugar.objects.all()
    context = {
        'sugar': sugar,
    }
    return render(request, 'order.html', context=context)
