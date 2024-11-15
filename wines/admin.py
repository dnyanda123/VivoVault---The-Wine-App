# In wines/admin.py
from django.contrib import admin
from .models import Wine

class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'vintage_year', 'region', 'rating', 'serving_temperature', 'Alcohol', 'Bottle_size')
    search_fields = ('name', 'type', 'region')
    list_filter = ('type', 'vintage_year', 'region')
    ordering = ('name', 'vintage_year')

# Register the model with the custom admin class
admin.site.register(Wine, WineAdmin)
