from django.db import models
class Country(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return "%s" %(self.name)

class State(models.Model):
    name = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    def __str__(self):
        return "%s" %(self.name)

class City(models.Model):
    name = models.CharField(max_length = 100)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    def __str__(self):
        return "%s" %(self.name)

    # def clean(self):
    #     if self.name:
             
    #         self.name = self.name.strip()