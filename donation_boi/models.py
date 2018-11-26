from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    location_type = models.CharField(max_length=60)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s at %s" % (self.name, self.address)