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


class Item(models.Model):
    ITEM_TYPE_CHOICES = (('clothing', 'Clothing'),
                        ('hat', 'Hat'),
                        ('kitchen', 'Kitchen'),
                        ('electronics', 'Electronics'),
                        ('household', 'Household'),
                        ('other', 'Other'),
                         )

    name = models.CharField(max_length=60)
    short_description = models.CharField(max_length=250)
    long_description = models.TextField()
    price = models.DecimalField(decimal_places=2, default=0, max_digits=6)
    category = models.CharField(choices=ITEM_TYPE_CHOICES,blank=False, max_length=120)
    store = models.ForeignKey(Store, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.store)