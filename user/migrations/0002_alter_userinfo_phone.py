# Generated by Django 4.2.6 on 2024-01-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(max_length=11),
        ),
    ]
