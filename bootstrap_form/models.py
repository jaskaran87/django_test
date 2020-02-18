from django.db import models
class ContactUs(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 100)
	address = models.CharField(max_length = 100)

	def __str__(self):
		return self.name