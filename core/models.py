from django.db import models

# Create your models here.

class usercontact(models.Model):
    
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    msn = models.TextField( max_length=300)

    def __str__(self):
        return self.name
