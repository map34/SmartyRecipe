from django.db import models


# Create your models here.
class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.recipeid} - {self.name}'


class Ingredient(models.Model):
    ingredientid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'<{self.ingredientid} - {self.name}>'


class Measure(models.Model):
    measureid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    short_name = models.CharField(max_length=20)

    def __str__(self):
        return f'<{self.measureid} - {self.name}>'
