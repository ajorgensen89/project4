# Generated by Django 3.2.19 on 2023-06-29 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_welcomemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WelcomeModel',
        ),
    ]