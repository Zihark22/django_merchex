# Generated by Django 5.0.1 on 2024-01-25 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
