from django.db import models

class Temperature(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'drinks'

    def__str__(self):
        return f'{self.name}'