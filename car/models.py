from django.db import models
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from PIL import Image
import uuid


class BaseModel(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now = True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True



class Category(BaseModel):
     name = models.CharField(max_length=255)
     slug = models.SlugField(null=True, blank=True)


     def __str__(self):
          return self.name


     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.name, allow_unicode=True)
          return super().save(*args, **kwargs)



class Brands(BaseModel):
     name = models.CharField(max_length=255)
     icon = models.ImageField(upload_to='brands/')

     class Meta:
          verbose_name = 'Brand'
          verbose_name_plural = 'Brands'


     def __str__(self):
          return self.name



class CarVilla(BaseModel):
     brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='brand_car')
     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_car')
     model = models.CharField(max_length=255)
     year = models.IntegerField(default=0)
     description = models.TextField()
     condition = models.CharField(max_length=255, verbose_name='qulayligi') ##qulayligi konditsioner bormi, yoqmi
     price = models.IntegerField(default=0, verbose_name='narxi')
     percentage = models.FloatField(default=0, verbose_name='chegirma')
     image = models.ImageField(upload_to='car_images/')
     videos = models.FileField(upload_to='car_videos/')
     dvigatel = models.CharField(max_length=255, verbose_name='matori')     ##elektrokarmi ili matormi 
     backer = models.CharField(max_length=255, verbose_name='karopkasi')    ##avtomatmi ili mexanikami
     views = models.IntegerField(default=0)



     def __str__(self):
          return f'{self.model} -- {self.brand.name} -- {self.category.name} -- {self.year} -- {self.price} -- {self.views}'


     @property
     def get_price(self):
          return self.price

     
     @property
     def get_new_price(self):
          if self.percentage:
               product_price = self.get_price
               discount = (100 - self.percentage) / 100 * product_price
               return round(discount, 2)
          return self.get_price



class CarImage(BaseModel):
    carvilla = models.ForeignKey(CarVilla, on_delete=models.CASCADE, related_name='car_images')
    image = models.ImageField(upload_to="car_images/")


    
    def __str__(self):
          return f"{self.carvilla}"

    @property
    def image_url(self):
          return self.image.url


    @property
    def get_image(self):
          if not self.image.url:
               return "No Image"
          return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))

    def save(self, *args, **kwargs):
          super().save(*args, **kwargs)
          img = Image.open(self.image.path)
          o_size = (405, 500)
          img.thumbnail(o_size)
          img.save(self.image.path, quality=50)