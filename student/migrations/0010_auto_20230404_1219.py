# Generated by Django 3.2.13 on 2023-04-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20230404_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netijeler',
            name='Dogry_sany',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netijeler',
            name='Yalnys_sany',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]