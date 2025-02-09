from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.title}, {self.salary}"