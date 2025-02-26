from django.db import models
from car.models import BaseModel



class Sevimlilar(BaseModel):
     # 2ta bashqa bashqa modellani (ForeignKey) bilan bog'lash 
     user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='author_sevimlilar')
     product = models.ForeignKey('car.CarVilla', on_delete=models.CASCADE, related_name='author_product')

     class Meta:
          unique_together = ("user", "product")


     def __str__(self):
          return f'{self.user} - {self.product}'



class AddToShopCart(BaseModel):
     user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='author_shopcart')
     product = models.ForeignKey('car.CarVilla', on_delete=models.CASCADE, related_name='shopcart_product')
     quantity = models.PositiveIntegerField(default=1)

     class Meta:
          unique_together = ("user", "product")

     def __str__(self):
          return f'{self.user} - {self.product} - {self.quantity}'
