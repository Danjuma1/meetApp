# Generated by Django 3.0.3 on 2020-03-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetappgroup',
            name='desc',
            field=models.TextField(help_text='Enter your group descriptions here...', max_length=1000),
        ),
    ]
