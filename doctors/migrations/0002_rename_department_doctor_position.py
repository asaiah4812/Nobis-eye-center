# Generated by Django 4.2.6 on 2023-10-07 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='department',
            new_name='position',
        ),
    ]
