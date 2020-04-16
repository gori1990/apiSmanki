from rest_framework import serializers
from .models import Dish, Category, Unit, Ingredients

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id,', 'name']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']

class IngredientsSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=True, read_only=True)
    class Meta:
        model = Ingredients
        fields = ['id','name', 'quantity','unit']



class DishSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    #unit = UnitSerializer(many=True, read_only=True)
    ingredients = IngredientsSerializer(many=True, read_only=True)
    class Meta:
        model = Dish
        fields = ['id', 'category','name', 'difficult', 'preparationTime', 'shortDiscription', 'description', 'photo',
                   'movie','ingredients']

class DishMiniSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Dish
        fields = ['id', 'category', 'name', 'shortDiscription', 'photo']

