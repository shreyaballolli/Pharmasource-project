# Generated by Django 4.0.1 on 2022-01-22 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_expiry_date_donor_expiry_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='donor',
            new_name='donor1',
        ),
    ]