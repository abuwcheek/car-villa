from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from car.models import BaseModel
from car.models import CarVilla
from users.models import User


class Sevimlilar(BaseModel):
     # 2ta bashqa bashqa modellani (ForeignKey) bilan bog'lash 
     user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='author_sevimlilar')
     product = models.ForeignKey('car.CarVilla', on_delete=models.CASCADE, related_name='author_product')

     class Meta:
          unique_together = ("user", "product")


     def __str__(self):
          return f'{self.user} - {self.product}'



class AddToShopCart(BaseModel):
     user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="author_shopcart")
     product = models.ForeignKey('car.CarVilla', on_delete=models.CASCADE, related_name="shopcart_product")
     quantity = models.PositiveIntegerField(default=1)

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
          return f"{self.user.username} - {self.product.model} - {self.quantity} ({self.status})"

     @property
     def total_price(self):
          return self.product.get_new_price * self.quantity



def validate_file_extension(value):
     allowed_formats = ["image/jpeg", "image/png", "application/pdf"]
     if hasattr(value.file, "content_type") and value.file.content_type not in allowed_formats:
          raise ValidationError("Faqat JPEG, PNG yoki PDF fayllarni yuklash mumkin!")



# ========== 4. To'lov modeli ==========
class Payment(BaseModel):
     order = models.ManyToManyField(AddToShopCart, related_name="payment")
     country = models.CharField(max_length=50)
     address = models.CharField(max_length=255)
     phone = models.CharField(max_length=13)

     payment_method = models.CharField(max_length=20, choices=[
          ("card", "Karta"),
          ("cash", "Naqd pul"),
          ("transfer", "O'tkazma"),
     ], default="cash")


     class Meta:
          verbose_name = "To'lov"
          verbose_name_plural = "To'lovlar"

     def __str__(self):
          return f"Payment {self.id} - {self.payment_method}"

     @property
     def total_price(self):
          return sum([item.total_price for item in self.order.all()])

     @property
     def get_buyer(self):
          return self.order.first().user.username if self.order.exists() else "-"