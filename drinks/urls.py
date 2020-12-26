from django.urls import path
from drinks.controllers import ice_controller, size_controller,splash_controller,sugar_controller, topping_controller,temperature_controller

urlpatterns = [
    path('', ourdrinks_controller.index, name='ourdrinks_list'),
]