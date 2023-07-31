from django.contrib import admin
from .models import Beverages, Candy, Snacks, WarmFood, Sundries, FrozenItems
# Register your models here.
admin.site.register(Beverages)
admin.site.register(Candy)
admin.site.register(Snacks)
admin.site.register(WarmFood)
admin.site.register(Sundries)
admin.site.register(FrozenItems)