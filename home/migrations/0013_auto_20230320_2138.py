# Generated by Django 3.2.13 on 2023-03-20 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20230317_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmaglumatlary',
            name='Topar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.toparlar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testmaglumatlary',
            name='Wagyt_limidi',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Aktiw',
        ),
    ]