from django.db import models

class Beverages(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SnackOnTheGo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Candy(models.Model):
    snack_on_the_go = models.ForeignKey(SnackOnTheGo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Snacks(models.Model):
    snack_on_the_go = models.ForeignKey(SnackOnTheGo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WarmFood(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Sundries(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class FrozenItems(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
