from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    CATEGORIES = (
        ('BRE', 'Breakfast'),
        ('SAL', 'Salad'),
        ('BEV', 'Beverages'),
    )
    category = models.CharField(max_length=3, choices=CATEGORIES, default='BEV')


class Order(models.Model):
    table_number = models.IntegerField()
    meals = models.ManyToManyField('Meal')

    @property
    def total_price(self):
        qs = self.meals.through.objects.all().aggregate(total_price=models.Sum('meal__price'))
        return qs['total_price']


