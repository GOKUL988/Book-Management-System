# Generated by Django 5.1.1 on 2025-04-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreapp', '0027_issue_ava_issue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='ava_issue',
            new_name='issued',
        ),
    ]
