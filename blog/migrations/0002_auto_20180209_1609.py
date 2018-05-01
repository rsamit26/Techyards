# Generated by Django 2.0.2 on 2018-02-09 16:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code_tags',
            field=models.CharField(choices=[('Python', 'python'), ('None', 'none'), ('Golang', 'golang'), ('c++', 'C++'), ('Generic', 'generic')], default='python', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 16, 9, 21, 741886, tzinfo=utc)),
        ),
    ]
