from apps.recipes.models import (Ingredient,
                                 Measure,
                                 Recipe)

from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('recipeid', 'name', 'description')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('ingredientid', 'name', 'description')


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ('measureid', 'name', 'description')
