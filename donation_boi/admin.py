from django.contrib import admin
from .models import Store, Item

class ItemAdmin(admin.ModelAdmin):
    fields = ["store", "name", "short_description", "long_description", "price", "category"]

class ItemInline(admin.StackedInline):
    model = Item
    number = 1

class StoreAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.site_header = "Donation Boi Admin"

admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
