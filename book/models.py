from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100),
    price = models.PositiveIntegerField(help_text='in cents'),
    weight = models.PositiveIntegerField(help_text='in grams')

    def __str__(self):
        return self.name


