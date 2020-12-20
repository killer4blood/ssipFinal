from django.db import models
from drinks.models.size import Size
from drinks.models.ice import Ice
from drinks.models.sugar import Sugar
from drinks.models.temperature import Temperature
from drinks.models.topping import Topping

class Splash(models.Model):
    name = models.CharField(max_length=100)
    sizes = models.ManyToManyField(Size)
    ice = models.ManyToManyField(Ice)
    sugar = models.ManyToManyField(Sugar)
    temperature = models.ManyToManyField(Temperature)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        app_label = 'drinks'

    def__str__(self):
        return f'{self.name}'