from django.db import models
from job.models import Job
from address.models import Address

class Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    adress = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.first_name}, Email:{self.email}, Phone: {self.phone}"

#should be my pull request