# Generated by Django 3.0.3 on 2020-02-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200224_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(null=True, related_name='interests', to='users.Interest'),
        ),
    ]
