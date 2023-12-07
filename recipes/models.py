from django.db import models

# Create your models here.
class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    COURSE_CHOICES = (
        ('Starters','Starters'),
        ('Main','Main'),
        ('Sides','Sides'),
        ('Dessert','Dessert'),
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Drinks','Drinks'),
        ('Vegetarian','Vegetarian'),
        # Add more cuisine choices here
        )
    
    # each class variable represents a database i.e. table field in the model
    recipe_name = models.CharField(max_length=200)
    recipe_creator = models.CharField(max_length=30)
    recipe_published_date = models.DateField('Recipe Published Date')
    ingredient =models.TextField(default='write your recipe')
    course = models.CharField(max_length=200, choices=COURSE_CHOICES)
    recipe_description = models.TextField(default='Share your secret recipe with the world!')
    cooking_time = models.IntegerField('Minutes')
    recipe_pic = models.ImageField(upload_to="images", default='null')  # Provide the default image path



    def __str__(self):
        return self.recipe_name + " - " + self.recipe_creator
        