from datetime import timezone
from django.db import models
import os

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    shape = models.CharField(max_length=20, choices=[('rectangular', 'Прямоугольный'), ('oval', 'Овальный')])
    horizontal_position = models.FloatField()
    vertical_position = models.FloatField()
    width_percent = models.FloatField()
    length_percent = models.FloatField()
    #class Meta: меняет названия в панели админа

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=os.path.join('config', 'menu_photos'), blank=True, null=True)   
    ingredients = models.TextField()
    description = models.TextField()
    recipe = models.TextField()

    
    def get_ingredients_list(self):
        # Возвращает список ингредиентов, разделенных по новой строке
        return [ingredient.strip() for ingredient in self.ingredients.split('\n') if ingredient.strip()]

    def __str__(self):
        return self.title
