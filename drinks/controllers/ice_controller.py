from django.shortcuts import render
from drinks.models.ice import Ice


def index(request):
    ice = Ice.objects.all()
    context = {
        'ice': ice,
    }
    return render(request, 'order.html', context=context)
