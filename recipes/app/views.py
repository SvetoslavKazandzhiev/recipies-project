from django.shortcuts import render, redirect

from app.forms import RecipesForm
from app.models import Recipes


def index(request):
    if Recipes.objects.all():
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def edit(request):
    return render(request, 'edit.html')


def create(request):
    if request.method == 'GET':
        context = {
            'form': RecipesForm(),
        }

        return render(request, 'create.html', context)
    else:
        form = RecipesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create.html')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


def delete_recipe(request):
    pass


def details(request):
    return render(request, 'details.html')