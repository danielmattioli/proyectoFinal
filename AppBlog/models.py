"""
from django.db import models

# Create your models here.
class cuenta(models.Model):
    user = models.CharField(max_lengh=30)
    email = models.EmailField(max_lengh=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user

"""
