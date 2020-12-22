from django.shortcuts import render
from drinks.models.size import Size


def index(request):
    size = Size.objects.all()
    context = {
        'size': size,
    }
    return render(request, 'order.html', context=context)
