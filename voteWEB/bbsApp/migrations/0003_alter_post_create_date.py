# Generated by Django 3.2.5 on 2022-03-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbsApp', '0002_auto_20220314_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
