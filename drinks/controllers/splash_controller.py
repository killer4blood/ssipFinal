from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from drinks.forms import makeyourownForm

def index(request):
    if request.method == 'POST':
        form = makeyourownForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('checkout'))
    else:
        form = makeyourownForm()
        
    context = {
        'form': form
    }
    return render(request, 'makeyourown_form.html', context=context)

def checkout(request):
    return render (request, 'splash/checkout.html')