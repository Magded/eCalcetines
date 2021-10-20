from django.contrib import admin
from main.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Producto,ProductoAdmin)