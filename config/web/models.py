from pydoc import describe
from django.db import models




class Products(models.Model):
    name = models.CharField(max_length=65)
    describtion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name