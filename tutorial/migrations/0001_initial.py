# Generated by Django 2.0.2 on 2018-02-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionTitle', models.CharField(max_length=250)),
                ('questionSlug', models.CharField(max_length=250)),
            ],
        ),
    ]
