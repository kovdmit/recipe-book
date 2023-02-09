# Generated by Django 4.1 on 2022-08-20 11:54

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Уникальное имя')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=255, verbose_name='Цитата')),
            ],
            options={
                'verbose_name': 'Цитата',
                'verbose_name_plural': 'Цитаты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('short_desc', models.TextField(verbose_name='Примечание')),
                ('proportions', models.TextField(verbose_name='Ингредиенты')),
                ('content', models.TextField(verbose_name='Пошаговый рецепт')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение (обложка)')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('published', models.BooleanField(default=False, verbose_name='👀')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipe.category', verbose_name='Категория')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
