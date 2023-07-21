
# Create your models here.
from django.db import models
from user.models import User

class Qualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.degree} - {self.user.name}"
