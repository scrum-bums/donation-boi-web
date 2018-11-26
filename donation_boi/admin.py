from django.contrib import admin
from .models import Store

# Register your models here.

admin.site.site_header = "Donation Boi Admin"

admin.site.register(Store)
