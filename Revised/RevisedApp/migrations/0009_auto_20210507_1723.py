# Generated by Django 3.1.7 on 2021-05-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevisedApp', '0008_auto_20210507_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'coordinator'), (2, 'Student'), (2, 'Guest')], default=2),
        ),
    ]
