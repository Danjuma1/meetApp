# Generated by Django 3.0.3 on 2020-02-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('location_address', models.CharField(max_length=255)),
                ('member_since', models.DateTimeField(auto_now_add=True, verbose_name='Account Since')),
                ('bio', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='', verbose_name='Profile Image')),
            ],
        ),
        migrations.CreateModel(
            name='GroupDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255)),
                ('group_location', models.CharField(max_length=255)),
                ('total_members', models.IntegerField()),
                ('group_about', models.CharField(max_length=255)),
                ('organizers', models.ManyToManyField(to='createGroup.Organizer')),
            ],
        ),
    ]
