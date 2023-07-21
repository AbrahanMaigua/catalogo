from django.contrib import admin
from .models import *

# Register your models here.

class CustomItemAdmin(admin.ModelAdmin):
    model = onder
    list_display = ('ID', 
                    'name',
                    'valor',
                    'fabricado',
                    'valido',
                    'imagen')
    list_filter = ("ID", 'valido')

class CustomOrderAdmin(admin.ModelAdmin):
    model = item
    list_display = ('order_id', "user_id")

class CustomCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(onder, CustomOrderAdmin)
admin.site.register(car, CustomCarAdmin)

admin.site.register(item, CustomItemAdmin)
