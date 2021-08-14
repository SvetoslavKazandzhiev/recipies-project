from django import forms

from app.models import Recipes


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'