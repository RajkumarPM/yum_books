# Generated by Django 2.1.15 on 2023-10-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20231026_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='cooking_time',
            field=models.IntegerField(verbose_name='Minutes'),
        ),
    ]