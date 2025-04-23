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
     quantity = models.PositiveIntegerField(default=1, max_length=3)

     STATUS_CHOICES = [
     ("to'lanmagan", "To'lanmagan"),
     ("tasdiqlangan", "Tasdiqlangan"),
     ("jo'natilgan", "Jo'natilgan"),
     ("yetkazilgan", "Yetkazilgan"),
     ("bekor qilingan", "Bekor qilingan"),
     ("qaytarilgan", "Qaytarilgan"),
     ]

     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="to'lanmagan")

     class Meta:
          unique_together = ("user", "product")

     def __str__(self):
          return f'{self.user} - {self.product} - {self.quantity}'



class Payment(BaseModel):
     order = models.ManyToManyField(AddToShopCart, related_name='payment')
     country = models.TextField()
     address = models.TextField()
     phone = models.CharField(max_length=13)


     def __str__(self):
          return self.order

     
     @property
     def total(self):
          total = 0 
          for order in self.order.all():
               total += order.product.get_new_price * order.quantity
          return total