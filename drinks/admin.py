from django.contrib import admin
from drinks.models import splash, ice, size, sugar, temperature, topping

# Register your models here.
admin.site.register(splash.Splash)
admin.site.register(ice.Ice)
admin.site.register(size.Size)
admin.site.register(sugar.Sugar)
admin.site.register(temperature.Temperature)
admin.site.register(topping.Topping)