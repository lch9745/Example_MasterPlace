from django.contrib import admin
from .models import Country_Data,City_Data,Place_Data
# Register your models here.
@admin.register(Country_Data)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'Data_id']



@admin.register(City_Data)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'Data_id']


@admin.register(Place_Data)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'Data_id']
