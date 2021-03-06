from django.db import models
from drinks.models.size import Size
from drinks.models.ice import Ice
from drinks.models.sugar import Sugar
from drinks.models.temperature import Temperature
from drinks.models.topping import Topping

class Splash(models.Model):
    name = models.CharField(max_length=100)
    sizes = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
    ice = models.ForeignKey(Ice, null=True, on_delete=models.SET_NULL)
    sugar = models.ForeignKey(Sugar, null=True, on_delete=models.SET_NULL)
    temperature = models.ForeignKey(Temperature, null=True, on_delete=models.SET_NULL)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        app_label = 'drinks'

    def __str__(self):
        return f'{self.name}'