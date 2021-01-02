from django.core.paginator import Paginator
from django.shortcuts import render
from drinks.models.topping import Topping


def index(request):
    toppings = Topping.objects.all()
    # we split our toppings into 4 each page
    paginator = Paginator(toppings, 4)  # change number based on your needs

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # instead of toppings, we pass page_obj to out HTML
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'topping/index.html', data)

