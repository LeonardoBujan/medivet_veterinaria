# Generated by Django 5.0.4 on 2024-05-09 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_alter_pet_options_alter_pet_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pet',
            table='pets',
        ),
    ]
