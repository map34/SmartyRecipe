from apps.recipes.views import (recipe_detail,
                                recipe_list)

from django.urls import path

urlpatterns = [
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
]
