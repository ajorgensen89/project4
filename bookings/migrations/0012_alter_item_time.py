# Generated by Django 3.2.19 on 2023-06-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_remove_item_tablesize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time',
            field=models.CharField(choices=[('5PM', '5PM'), ('6PM', '6PM'), ('7PM', '7PM'), ('8PM', '8PM'), ('9PM', '9PM'), ('10PM', '10PM'), ('11PM', '11PM')], default='5PM', max_length=8),
        ),
    ]
