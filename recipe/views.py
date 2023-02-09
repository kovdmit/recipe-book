from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from taggit.models import Tag

from .models import *
from .forms import RecipeForm, UserLoginForm


# class Index(ListView):
#     model = Recipe
#     template_name = 'recipe/index.html'
#     context_object_name = 'recipe'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Книга рецептов'
#         return context
#
#     def get_queryset(self):
#         return Recipe.objects.filter(published=True)


def index(request, tag_id=None, category_slug=None):
    recipe = Recipe.objects.filter(published=True)
    tag = None
    category = None

    if tag_id:
        tag = get_object_or_404(Tag, pk=tag_id)
        recipe = recipe.filter(tags__in=[tag])

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        recipe = recipe.filter(category__in=[category])

    paginator = Paginator(recipe, 9)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не INT, то включить 1ю страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, отобразить последнюю страницу.
        posts = paginator.page(paginator.num_pages)

    context = {
        # 'recipe': recipe,
        'title': 'Книга рецептов',
        'categories': Category.objects.all(),
        'page': page,
        'posts': posts,
        'tag': tag,
        'category': category,
    }
    return render(request, 'recipe/recipe/index.html', context=context)


# class Cat(ListView):
#     model = Recipe
#     template_name = 'recipe/category.html'
#     context_object_name = 'recipe'
#
#     def get_queryset(self):
#         return Recipe.objects.filter(category=self.kwargs['category_slug'], published=True)


def recipe_view(request, recipe_slug):
    recipe_full = Recipe.objects.get(slug=recipe_slug)

    post_tags_ids = recipe_full.tags.values_list('id', flat=True)
    similar_posts = Recipe.objects.filter(tags__in=post_tags_ids).exclude(id=recipe_full.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-create_at')[:3]

    context = {
        'recipe_full': recipe_full,
        'similar_posts': similar_posts,
    }
    return render(request, 'recipe/recipe/recipe.html', context=context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # recipe = Recipe.objects.create(**form.cleaned_data)
            recipe = form.save()
            return redirect(recipe)
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe/add_recipe.html', {'form': form})


def about(request):
    return render(request, 'recipe/recipe/about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успех!')
            return redirect('home')
        else:
            messages.error(request, 'Неудача!')
    else:
        form = UserCreationForm()
    return render(request, 'recipe/recipe/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'recipe/recipe/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class Search(ListView):
    template_name = 'recipe/recipe/index.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['title'] = f"Поиск по запросу: {self.request.GET.get('s')}"
        return context