# Generated by Django 3.2.19 on 2023-06-24 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cancel',
        ),
    ]
