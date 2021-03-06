from django.db import models
from django.contrib.auth.models import User 

class UserR(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
