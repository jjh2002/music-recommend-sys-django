# Generated by Django 4.2.6 on 2024-01-30 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_music_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
