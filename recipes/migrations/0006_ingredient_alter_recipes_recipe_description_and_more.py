# Generated by Django 4.2.6 on 2023-11-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipes_recipe_description_recipes_recipe_pic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_description',
            field=models.TextField(default='Share your secret recipe with the world!'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_pic',
            field=models.ImageField(default='null', upload_to='images'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.ingredient'),
        ),
    ]
