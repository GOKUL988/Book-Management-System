# Generated by Django 5.1.1 on 2025-04-01 13:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreapp', '0013_alter_supplier_sup_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='cno3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libreapp.supplier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='cno',
            field=models.UUIDField(default=uuid.UUID('bf2bb6a1-a3fd-414d-a5f4-27c80179b0ee'), editable=False),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_id',
            field=models.UUIDField(default=uuid.UUID('af29310f-e603-4f12-bf54-c9da7b3e7722'), editable=False, primary_key=True, serialize=False),
        ),
    ]
