# Generated by Django 4.1.7 on 2023-04-03 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
        ('login', '0005_user_theme_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='theme_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='used_theme', to='theme.theme'),
        ),
    ]
