from django import forms
from .models import Recipes  # Import your Recipes model

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes  # Associate the form with the Recipes model
        fields = '__all__'  # You can specify the fields you want to include, or use '__all__' for all fields