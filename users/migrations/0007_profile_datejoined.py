# Generated by Django 3.0.3 on 2020-02-27 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200227_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='datejoined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
