from django.shortcuts import render
# we import the models here, usually only one model
from drinks.models.splash import Splash


def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        # POST, get the request body parameter and filter the drink
        name = req['name']
        splashes = Splash.objects.filter(name__contains=name)
    else:
        splashes = Splash.objects.all()  # get all splashes
    # put in data dictionary
    context = {
        'splashes': splashes,
    }
    # render to our html
    return render(request, 'splash/index.html', context=context)

