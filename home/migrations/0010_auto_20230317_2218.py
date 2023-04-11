# Generated by Django 3.2.13 on 2023-03-17 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_testmaglumatlary_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sorag_sany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sorag_sany', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wagt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Wagyt_limidi', models.PositiveIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='toparlar',
            old_name='Topar',
            new_name='Toparlar',
        ),
        migrations.RemoveField(
            model_name='testmaglumatlary',
            name='Topar',
        ),
        migrations.RemoveField(
            model_name='testmaglumatlary',
            name='Wagyt_limidi',
        ),
        migrations.CreateModel(
            name='Aktiw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sorag_sany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sorag_sany')),
                ('Toparlar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.toparlar')),
                ('Wagt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wagt')),
            ],
        ),
    ]