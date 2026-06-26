from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin

from users.managers import CustomUserManager


class CustomUser(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # пользователь неактивен при регистрации

    objects=CustomUserManager

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email or ""



class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="confirmation")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.code = str(random.randint(100000, 999999))
        self.save()


