# Generated by Django 5.1 on 2024-08-21 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dining', '0004_expences'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expences',
            new_name='Expenses',
        ),
    ]