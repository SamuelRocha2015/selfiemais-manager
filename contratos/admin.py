from django.contrib import admin
from .models import Item, Orcamento, Plano

# Register your models here.

models = [Item, Plano, Orcamento]
admin.site.register(models)