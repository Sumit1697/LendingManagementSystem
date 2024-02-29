from django.db import models
from django.utils import timezone

# Create your models here.

class CifUserDetail(models.Model):
    id = models.BigAutoField(primary_key = True)
    cif_id = models.CharField(max_length=100, unique=True)
    external_id = models.CharField(max_length=100, unique=True)
    email_id = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique = True)
    pan_number = models.CharField(max_length=10, unique=True)
    date_of_birth = models.CharField(max_length=100)
    profile_type = models.CharField(max_length=20)
    user_address = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.cif_id} {self.external_id} {self.email_id} {self.mobile_number} {self.pan_number} {self.date_of_birth} {self.profile_type} {self.user_address} {self.created_at} {self.updated_at}"


class ProductConfig(models.Model):
    id = models.BigAutoField(primary_key = True)
    product_id = models.BigIntegerField(unique=True)
    version = models.SmallIntegerField(unique=True)
    config = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.product_id} {self.version} {self.config} {self.created_at} {self.updated_at}"
