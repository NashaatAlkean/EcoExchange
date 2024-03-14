from django.contrib import admin

# Register your models here.

from .models import Items,Catagory,City

admin.site.register(Items)
admin.site.register(Catagory)
admin.site.register(City)

