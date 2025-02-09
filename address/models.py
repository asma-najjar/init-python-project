from django.db import models

class Address(models.Model):
    city = models.CharField(max_length= 30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
