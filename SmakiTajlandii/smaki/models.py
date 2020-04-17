from django.db import models

GR = 'Gr'
ML = 'Ml'
KG = 'Kg'


units = (
    (GR, GR),
    (ML, ML),
    (KG, KG)
)


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Ingredients'

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
    ingredients = models.ManyToManyField(Ingredients, through='Unit')

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name


class Unit(models.Model):
    unit = models.CharField(max_length=128, choices=units, null=True, blank=True)
    quantity = models.CharField(max_length=128, blank=True, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.unit
