from django.db import models
from drinks.models.temperature import Temperature
from drinks.models.topping import Topping

class ourDrinks(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.ForeignKey(Temperature, null=True, on_delete=models.SET_NULL)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        app_label = 'drinks'

    def __str__(self):
        return f'{self.name}'