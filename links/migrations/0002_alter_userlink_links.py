# Generated by Django 4.1.7 on 2023-03-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlink',
            name='links',
            field=models.URLField(max_length=400),
        ),
    ]