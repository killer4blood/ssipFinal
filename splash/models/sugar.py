from djago.db import models

class Sugar(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'splash'

    def__str__(self):
        return f'{self.name}'