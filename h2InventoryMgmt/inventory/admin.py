from django.contrib import admin
from .models import Beverage, Candy, Snack, WarmFood, Sundrie, FrozenItem
# Register your models here.
admin.site.register(Beverage)
admin.site.register(Candy)
admin.site.register(Snack)
admin.site.register(WarmFood)
admin.site.register(Sundrie)
admin.site.register(FrozenItem)