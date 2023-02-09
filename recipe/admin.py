from django.contrib import admin
from django import forms
from .models import Recipe, Category, Quote

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget




class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Пошаговый рецепт')
    short_desc = forms.CharField(widget=CKEditorWidget(), label='Примечание')
    proportions = forms.CharField(widget=CKEditorWidget(), label='Ингредиенты')

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'create_at', 'author', 'views', 'published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category')
    list_filter = ('category',)
    fields = (
    'title', 'slug', 'short_desc', 'proportions', 'content', 'photo', 'author', 'published', 'category', 'tags', 'create_at', 'views',)
    readonly_fields = ('create_at', 'views',)
    save_on_top = True
    save_as = True
    list_editable = ('published',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quote)


'''

©

'''
