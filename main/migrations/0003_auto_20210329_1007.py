# Generated by Django 3.1.2 on 2021-03-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bookshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
