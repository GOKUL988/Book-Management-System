# Generated by Django 5.1.1 on 2025-03-02 11:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreapp', '0002_alter_purchase_bill_alter_supplier_sup_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='sup_id',
            field=models.UUIDField(default=uuid.UUID('ce3b17ad-5f87-4df9-bd4d-a8dedfb6ff17'), editable=False, primary_key=True, serialize=False),
        ),
    ]
