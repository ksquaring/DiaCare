# Generated by Django 3.2.15 on 2023-03-05 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230305_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodchoice',
            name='quantity',
            field=models.CharField(default='1', max_length=255),
        ),
        migrations.AddField(
            model_name='producechoice',
            name='quantity',
            field=models.CharField(default='1', max_length=255),
        ),
    ]