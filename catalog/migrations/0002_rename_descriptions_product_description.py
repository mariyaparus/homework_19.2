# Generated by Django 4.2.4 on 2023-09-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptions',
            new_name='description',
        ),
    ]
