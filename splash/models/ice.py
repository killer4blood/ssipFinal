from djago.db import models

class Ice(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'splash'

    def__str__(self):
        return f'{self.name}'