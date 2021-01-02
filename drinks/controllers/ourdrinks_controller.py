from django.core.paginator import Paginator
from django.shortcuts import render
from drinks.models.ourdrinks import ourDrinks


def index(request):
    ourdrinks = ourDrinks.objects.all()
    paginator = Paginator(ourdrinks, 4)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'ourdrinks/index.html', context=context)
