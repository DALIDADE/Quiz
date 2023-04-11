# Generated by Django 3.2.13 on 2023-03-10 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_remove_testmaglumatlary_sorag_sany'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmaglumatlary',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]