from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body']
    search_fields = ['title','body']
    ordering = ['title','body']


admin.site.register(Data, DataAdmin)