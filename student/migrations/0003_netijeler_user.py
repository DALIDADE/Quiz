# Generated by Django 3.2.13 on 2023-04-01 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_auto_20230331_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='netijeler',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]