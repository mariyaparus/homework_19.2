# Generated by Django 4.2.4 on 2023-09-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_updated',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
