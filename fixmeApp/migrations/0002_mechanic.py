# Generated by Django 5.1.4 on 2024-12-16 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Please enter a valid email address')])),
                ('location', models.CharField(max_length=30)),
                ('experience', models.SmallIntegerField(default=0)),
                ('phone', models.CharField(max_length=14, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(14)])),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
