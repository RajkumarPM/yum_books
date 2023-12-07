from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipes
from .forms import RecipesForm

def index(request):
    newest_recipes = Recipes.objects.order_by('-recipe_published_date')[:15]
    context = {'newest_recipes': newest_recipes}
    return render(request, 'recipes/index.html', context)

def show(request, recipe_id):
    try:
        recipe = Recipes.objects.get(pk=recipe_id)
    except Recipes.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/show.html', {'recipe': recipe})

def create_recipe(request):
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data as a new Recipes instance
            newest_recipes = Recipes.objects.order_by('-recipe_published_date')[:15]
            context = {'newest_recipes': newest_recipes}
            return render(request, 'recipes/index.html', context)
    else:
        form = RecipesForm()

    return render(request, 'recipes/create_recipe.html', {'form': form})

def edit_recipe(request, recipe_id):
    # Get the recipe to edit or return a 404 page if it doesn't exist
    recipe = get_object_or_404(Recipes, pk=recipe_id)

    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()  # Save the updated form data to the recipe
            return redirect('recipes:show', recipe_id=recipe_id)
    else:
        # Create a form with the existing recipe data
        form = RecipesForm(instance=recipe)

    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})


def delete_recipe(request, recipe_id):
    try:
        recipe = Recipes.objects.get(pk=recipe_id)
    except Recipes.DoesNotExist:
        raise Http404("Recipe does not exist")

    if request.method == 'POST':
        recipe.delete()  # Delete the recipe
        return redirect('recipes:index')  # Redirect to the recipe list (index) page

    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})

