from django.db import models
from django.utils import timezone

# Create your models here.

class usercontact(models.Model):
    
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    msn = models.TextField( max_length=400)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
