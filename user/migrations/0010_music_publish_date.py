# Generated by Django 4.2.6 on 2024-01-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_music_pic_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]