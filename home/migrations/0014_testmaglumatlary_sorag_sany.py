# Generated by Django 3.2.13 on 2023-03-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20230320_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmaglumatlary',
            name='Sorag_sany',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]