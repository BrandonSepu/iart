from django.db import models
from django.utils import timezone

# Create your models here.

class usercontact(models.Model):
    
    nameContact = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    msn = models.TextField( max_length=400)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nameContact



class typeProduct (models.Model) :
    nomType = models.CharField( max_length = 50)
    descriptionType = models.TextField(max_length=400)
    def __str__(self):
        return self.nomType

class statusProduct (models.Model) :
    nomStatus = models.CharField( max_length = 20)
    descriptionStatus = models.TextField(max_length=400)
    def __str__(self):
        return self.nomStatus    


class newProduct(models.Model):  

    type = models.ForeignKey(typeProduct, on_delete=models.CASCADE)
    ancho = models.IntegerField()
    largo = models.IntegerField()
    price = models.IntegerField()
    status = models.ForeignKey(statusProduct, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    img = models.ImageField(upload_to='img_productos', null=True, blank=True)

    def __str__(self):
        return self.description

class gender(models.Model):
    nomGender = models.CharField( max_length = 10)

    def __str__(self):
        return self.nomGender

class extraDataUser(models.Model):
    wsp = models.IntegerField()
    birthday = models.DateTimeField(default=timezone.now)
    genderuser = models.ForeignKey(gender, on_delete=models.CASCADE)
    instagram = models.CharField(max_length = 30)

    def __str__(self):
        return self.instagram


'''
    class CustomUserCreationForm(UserCreationForm):
        class Meta : 
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
'''
