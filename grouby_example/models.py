from django.db import models
from country.models import Country

class City(models.Model):
	name = models.CharField(max_length = 30)
	country = models.ForeignKey(Country, on_delete= models.CASCADE) # ForeignKey
	population = models.PositiveIntegerField()

