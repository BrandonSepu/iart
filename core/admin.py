from django.contrib import admin
from .models import usercontact, newProduct, statusProduct, typeProduct, comuna, extraDataUser, \
     gender, pais, region, order
# Register your models here.

class userscontact(admin.ModelAdmin):
    list_display = ["nameContact", "email", "msn", "created_date"]
    search_fields = ["nom"]

class sProduct(admin.ModelAdmin):
    list_display = ["nomStatus", "descriptionStatus"]
    search_fields = ["nomStatus"]

class tProduct(admin.ModelAdmin):
    list_display = ["nomType", "descriptionType"]
    search_fields = ["nomType"]

class nProduct(admin.ModelAdmin):
    list_display = ["type", "price", "ancho", "largo", "status", "description", "img"]
    search_fields = ["description"]

# Register your models here.

admin.site.register(usercontact, userscontact)
admin.site.register(newProduct, nProduct)
admin.site.register(typeProduct, tProduct)
admin.site.register(statusProduct, sProduct)
admin.site.register(comuna)
admin.site.register(extraDataUser)
admin.site.register(gender)
admin.site.register(pais)
admin.site.register(region)
admin.site.register(order)