# Generated by Django 4.2.15 on 2024-08-17 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
    ]
