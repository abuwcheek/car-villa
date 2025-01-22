from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)
    image_user = models.ImageField(upload_to='user_avatar/', null=True, blank=True,
                                   validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'heic', 'jpeg', 'svg', 'img'))])

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def hashin_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        self.hashin_password()
        return super().save(*args, **kwargs)