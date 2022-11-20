from django.urls import path
from calculator.views import hello, recipe_products


urlpatterns = [
    path('', hello, name='hello'),
    path('<dish_name>/', recipe_products),
]
