# Generated by Django 4.2.5 on 2024-10-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('carbohydrates', 'Carbohydrates'), ('proteins', 'Proteins'), ('fats', 'Fats'), ('vitamins', 'Vitamins'), ('minerals', 'Minerals'), ('water', 'Water')], max_length=20)),
                ('calories', models.FloatField()),
                ('protein', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('carbohydrates', models.FloatField(blank=True, null=True)),
                ('vitamins', models.TextField(blank=True, null=True)),
                ('minerals', models.TextField(blank=True, null=True)),
                ('water_content', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
