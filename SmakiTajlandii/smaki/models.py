from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name



class Ingredients(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    #unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=128)
    difficult = models.IntegerField(default=1)
    preparationTime = models.IntegerField(blank=True, null=True, )
    shortDiscription = models.TextField(default='')
    description = models.TextField(default='')
    photo = models.ImageField(upload_to="images", blank=True, )
    movie = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredients, through='unit' )
    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=128)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name