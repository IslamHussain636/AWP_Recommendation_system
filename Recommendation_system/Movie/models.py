from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
