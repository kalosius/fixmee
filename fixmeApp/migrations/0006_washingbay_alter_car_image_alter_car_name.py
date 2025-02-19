# Generated by Django 5.1.4 on 2024-12-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmeApp', '0005_remove_car_model_name_car_model_car_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WashingBay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
