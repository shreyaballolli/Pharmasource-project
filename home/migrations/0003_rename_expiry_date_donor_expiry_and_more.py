# Generated by Django 4.0.1 on 2022-01-22 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_donor_delete_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='Expiry_date',
            new_name='Expiry',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='Product_description',
            new_name='desc',
        ),
    ]
