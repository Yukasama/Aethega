# Generated by Django 4.0.4 on 2022-05-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0005_financials_depreciationandamortization_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Financials',
            new_name='Financial',
        ),
    ]
