from apps.recipes.models import Recipe
from apps.recipes.serializers import RecipeSerializer

from django.test import TestCase


class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(name='Test Recipe',
                              description='This is a test recipe')
        Recipe.objects.create(name='Test Recipe2',
                              description='This is test recipe 2')

    def test_recipe_serialization_get(self):
        recipe1 = Recipe.objects.get(name='Test Recipe')
        recipe2 = Recipe.objects.get(name='Test Recipe2')
        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        self.assertEqual(serializer1.data['name'], 'Test Recipe')
        self.assertEqual(serializer2.data['name'], 'Test Recipe2')
