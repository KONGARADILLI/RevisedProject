# Generated by Django 3.1.7 on 2021-05-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevisedApp', '0006_delete_improfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinfo',
            name='year_of_pass',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
