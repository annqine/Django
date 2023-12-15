from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    shape = models.CharField(max_length=20, choices=[('rectangular', 'Прямоугольный'), ('oval', 'Овальный')])
    horizontal_position = models.FloatField()
    vertical_position = models.FloatField()
    width_percent = models.FloatField()
    length_percent = models.FloatField()

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
