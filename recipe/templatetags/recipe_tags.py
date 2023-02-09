from django import template
from recipe.models import Quote, Category
from random import randint


register = template.Library()


@register.simple_tag()
def get_quote():
    return Quote.objects.get(pk=randint(1, Quote.objects.count())).quote


@register.inclusion_tag('recipe/inc/show_cat.html')
def show_cat():
    return {'all_cat': Category.objects.all()}
