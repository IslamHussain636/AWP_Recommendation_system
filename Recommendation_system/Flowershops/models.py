from django.db import models

class FlowerShop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

