from django.shortcuts import render
from drinks.models.temperature import Temperature


def index(request):
    temperature = Temperature.objects.all()
    context = {
        'temperature': temperature,
    }
    return render(request, 'order.html', context=context)
