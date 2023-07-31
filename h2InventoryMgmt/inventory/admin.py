from django.contrib import admin
from .models import Beverage, Candy, Snack, WarmFood, Sundry, FrozenItem
# Register your models here.
admin.site.register(Beverage)
admin.site.register(Candy)
admin.site.register(Snack)
admin.site.register(WarmFood)
admin.site.register(Sundry)
admin.site.register(FrozenItem)