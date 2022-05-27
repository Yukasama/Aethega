# Generated by Django 4.0.4 on 2022-05-26 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0003_alter_info_logo_alter_info_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('costOfRevenue', models.IntegerField(blank=True, null=True)),
                ('grossProfit', models.IntegerField(blank=True, null=True)),
                ('grossProfitRatio', models.IntegerField(blank=True, null=True)),
                ('researchAndDevelopmentExpenses', models.IntegerField(blank=True, null=True)),
                ('generalAndAdministrativeExpenses', models.IntegerField(blank=True, null=True)),
                ('sellingAndMarketingExpenses', models.IntegerField(blank=True, null=True)),
                ('sellingGeneralAndAdministrativeExpenses', models.IntegerField(blank=True, null=True)),
                ('otherExpenses', models.IntegerField(blank=True, null=True)),
                ('operatingExpenses', models.IntegerField(blank=True, null=True)),
                ('costAndExpenses', models.IntegerField(blank=True, null=True)),
                ('netIncome', models.IntegerField(blank=True, null=True)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eye.stock')),
            ],
        ),
        migrations.DeleteModel(
            name='Cashflow',
        ),
    ]
