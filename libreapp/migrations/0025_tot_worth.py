# Generated by Django 5.1.1 on 2025-04-19 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreapp', '0024_stock_isbn_stock_qun_stock_rack'),
    ]

    operations = [
        migrations.CreateModel(
            name='tot_worth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField(default=0)),
                ('bookdt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreapp.stock')),
            ],
        ),
    ]
