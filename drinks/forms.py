from django.forms import ModelForm
from django.core.exceptions import ValidationError
from drinks.models.splash import Splash

class makeyourownForm(ModelForm):
    class Meta:
        model = Splash  # model to use in form
        # list of fields to be displayed
        fields = ['name', 'sizes', 'ice', 'sugar', 'temperature', 'toppings']