from django import forms
from .models import Recipe

from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RecipeForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Recipe
        fields = [
            'title', 'slug', 'short_desc', 'proportions', 'content', 'author', 'photo', 'category', 'tags'
        ]
        widgets = {

            'category': forms.Select(attrs={"class": "form-control", "placeholder": "Категория"}),

            'title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Наименование"}),

            'slug': forms.TextInput(attrs={"class": "form-control", "placeholder": "Уникальное имя"}),

            'short_desc': forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Примечание"}),

            'proportions': forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Ингредиенты"}),

            'content': forms.Textarea(attrs={"class": "form-control", "placeholder": "Пошаговый рецепт"}),

            'author': forms.TextInput(attrs={"class": "form-control", "placeholder": "Автор"}),

            'tags': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ключевые слова (через запятую)"}),

        }







'''
class RecipeForm(forms.Form):
    title = forms.CharField(max_length=255, label='Наименование', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Наименование",
    }))

    slug = forms.SlugField(max_length=255, label='Уникальное имя', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Уникальное имя",
    }))

    short_desc = forms.CharField(max_length=255, label='Примечание', widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
        "placeholder": "Примечание",
    }))

    proportions = forms.CharField(label='Ингредиенты', widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
        "placeholder": "Ингредиенты",
    }))

    content = forms.CharField(label='Пошаговый рецепт', widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Пошаговый рецепт",
    }))
    # photo = forms.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)

    author = forms.CharField(max_length=50, label='Автор', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Автор",
    }))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={
        "class": "form-control",
        "placeholder": "Категория",
    }))
'''
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, label='Ключевые слова', widget=forms.TextInput(attrs={
    #     "class": "form-control",
    #     "placeholder": "Ключевые слова",
    # }))
