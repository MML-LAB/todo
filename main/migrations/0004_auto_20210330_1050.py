# Generated by Django 3.1.2 on 2021-03-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210329_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshop',
            name='year',
            field=models.DateField(verbose_name='Год выхоа книги'),
        ),
    ]
