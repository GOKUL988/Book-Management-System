# Generated by Django 5.1.1 on 2025-04-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreapp', '0029_alter_issue_issued'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='paymth',
            field=models.CharField(default='Cash', max_length=10),
        ),
    ]
