from django.urls import path
from drinks.controllers import ice_controller, size_controller,splash_controller,sugar_controller, topping_controller,temperature_controller,ourdrinks_controller

urlpatterns = [
    path('', ourdrinks_controller.index, name='ourdrinks_list'),
    path('', topping_controller.index, name='topping_list'),
    path('', ice_controller.order, name='ice_list'),
    path('', size_controller.order, name='size_list'),
    path('', sugar_controller.order, name='sugar_list'),
    path('', splash_controller.index, name='splash'),
]