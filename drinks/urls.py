from django.urls import path
from drinks.controllers import ice_controller, size_controller,splash_controller,sugar_controller, topping_controller,temperature_controller

urlpatterns = [
    path('', splash_controller.index, name='splash_index'),
    path('ice', ice_controller.index, name='ice_index'),
    path('sugar', sugar_controller.index, name='sugar_index'),
    path('size', size_controller.index, name='size_index'),
    path('topping', topping_controller.index, name='topping_index'),
    path('temperature', temperature_controller.index, name='temperature_index'),
]