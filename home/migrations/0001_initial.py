# Generated by Django 3.2.13 on 2023-02-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultedlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fakultedin_ady', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sapaklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sapagyn_ady', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Toporlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topar', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestGosmak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Soragy', models.TextField()),
                ('a', models.CharField(max_length=100)),
                ('b', models.CharField(max_length=100)),
                ('c', models.CharField(max_length=100)),
                ('d', models.CharField(max_length=100)),
                ('Sapak_ady', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sapaklar')),
            ],
        ),
    ]
