# Generated by Django 4.1.7 on 2023-03-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0003_usersocials_position_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersocials',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='usersocials',
            name='position',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
