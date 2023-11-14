from django.db import models

# Create your models here.
class Fashion(models.Model):
    fashion_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)  # Assuming a comma-separated list of categories
    brand = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

