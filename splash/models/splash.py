from djago.db import models

class Splash(models.Model):
    name = models.CharField(max_length=100)
    sizes = models.ManyToManyField(Size)
    ice = models.ManyToManyField(Ice)
    sugar = models.ManyToManyField(Sugar)
    temperature = models.ManyToManyField(Temperature)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        app_label = 'splash'

    def__str__(self):
        return f'{self.name}'