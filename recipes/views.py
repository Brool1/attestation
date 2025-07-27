from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, RegisterForm
from .forms import RecipeForm
from django.contrib.auth import login
import random

def home(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 5))
    return render(request, 'recipes/home.html', {'recipes': random_recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
