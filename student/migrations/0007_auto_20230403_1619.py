# Generated by Django 3.2.13 on 2023-04-03 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0006_auto_20230403_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netijeler',
            name='Dogry_goterim',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='netijeler',
            name='Dogry_sany',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='netijeler',
            name='Yalnys_goterim',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='netijeler',
            name='Yalnys_sany',
            field=models.SmallIntegerField(),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topar', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
