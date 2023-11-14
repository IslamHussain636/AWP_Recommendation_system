from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

