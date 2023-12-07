# Generated by Django 4.2.6 on 2023-11-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_ingredient_alter_recipes_recipe_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredient',
            field=models.TextField(default='write your recipe'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]