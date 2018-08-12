from apps.recipes.models import (Ingredient,
                                 Measure,
                                 Recipe)

from django.contrib import admin


class RecipeAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


class MeasureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Measure, MeasureAdmin)
