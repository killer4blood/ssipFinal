from django.urls import path
from drinks.controllers import ice_controller, size_controller,splash_controller,sugar_controller, topping_controller,temperature_controller,ourdrinks_controller

urlpatterns = [
    path('', ourdrinks_controller.index, name='ourdrinks_list'),
    path('toppings', topping_controller.index, name='topping_list'),
    path('make-your-own', splash_controller.index, name='makeyourown'),
    path('checkout', splash_controller.checkout, name='checkout'),
]