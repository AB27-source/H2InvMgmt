# Generated by Django 4.2.3 on 2023-07-31 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_snack_rename_beverages_beverage_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sundrie',
            new_name='Sundry',
        ),
    ]
