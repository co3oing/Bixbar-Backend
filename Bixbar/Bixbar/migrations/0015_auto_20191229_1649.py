# Generated by Django 2.2.4 on 2019-12-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bixbar', '0014_recipemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='cocktail',
            field=models.ManyToManyField(to='bixbar.Cocktail'),
        ),
    ]
