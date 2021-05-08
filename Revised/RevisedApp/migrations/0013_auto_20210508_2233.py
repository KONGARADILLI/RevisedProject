# Generated by Django 3.1.7 on 2021-05-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevisedApp', '0012_coordinator_cord_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'coordinator'), (2, 'Student'), (3, 'Guest')], default=3),
        ),
    ]
