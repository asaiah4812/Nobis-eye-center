# Generated by Django 4.2.6 on 2023-10-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_message_alter_book_email_alter_service_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='body',
            field=models.TextField(blank=True, max_length=3000),
        ),
    ]
