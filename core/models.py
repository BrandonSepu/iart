from ast import Num
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


class pais(models.Model):
    
    nomPais = models.CharField(max_length=50)

    def __str__(self):
        return self.nomPais

    
class region(models.Model):

    fkPais = models.ForeignKey(pais, on_delete=models.CASCADE)
    nomRegion = models.CharField(max_length=50)

    def __str__(self):
        return self.nomRegion

class comuna(models.Model):

    fkRegion = models.ForeignKey(region, on_delete=models.CASCADE)
    nomComuna = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nomComuna

class extraDataUser(models.Model):
    userid = models.IntegerField(blank=True)
    wsp = models.IntegerField(blank=True)
    birthday = models.DateTimeField(default=timezone.now, blank=True)
    genderuser = models.ForeignKey(gender, on_delete=models.CASCADE, blank=True)
    instagram = models.CharField(max_length = 30, blank=True)
    comunaUser = models.ForeignKey(comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.instagram


'''class adress(models.Model):

    fkComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comentario = models.CharField(max_length=50, blank=True)

    def adressComplete(self):
        return "{},{}".format(self.calle, self.numero)

    def __str__(self):
        return self.adressComplete
'''
class order(models.Model):
    
    fkComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comentario = models.CharField(max_length=50, blank=True)
    Nombre = models.CharField(max_length=50)
    nro_contacto = models.IntegerField()
    instagram = models.CharField(max_length=50, blank=True)
    imagen_link = models.TextField(max_length=1000, blank=True)
    img = models.ImageField(upload_to='img_pedido', null=True, blank=True)
    type = models.ForeignKey(typeProduct, on_delete=models.CASCADE)
    ancho = models.IntegerField()
    largo = models.IntegerField()

    
    def __str__(self):
        return self.Nombre


'''
    class CustomUserCreationForm(UserCreationForm):
        class Meta : 
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
'''
