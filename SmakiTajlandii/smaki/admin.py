from django.contrib import admin
from .models import Dish, Category, Unit, Ingredients


class UnitInLine(admin.TabularInline):
    model = Unit
    extra = 0
    fields = ('ingredients', 'quantity', 'unit')
    verbose_name_plural = 'Ingredients'
    verbose_name = 'Ingredient'


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = (UnitInLine,)
    list_display = ['name', 'preparationTime', 'shortDiscription']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name']
