from django.db import models
from car.models import BaseModel, CarVilla


class Sevimlilar(BaseModel):
     user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='author_sevimlilar')
     product = models.ForeignKey(CarVilla, on_delete=models.CASCADE, related_name='author_product')


     def __str__(self):
          return f'{self.author} - {self.product}'
