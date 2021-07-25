from django.contrib import admin
from .models import usercontact
# Register your models here.

class userscontact(admin.ModelAdmin):
    list_display = ["name", "email", "msn", "created_date"]
    search_fields = ["nom"]

# Register your models here.

admin.site.register(usercontact, userscontact)