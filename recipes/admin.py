from django.contrib import admin
from .models import Recipes

# Register the model
#admin.site.register(Recipes)

# Define a custom admin class for the model
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_creator', 'recipe_published_date', 'ingredient', 'course', 'recipe_description', 'cooking_time', 'recipe_pic')

# Associate the custom admin class with the model
admin.site.register(Recipes, RecipesAdmin)
