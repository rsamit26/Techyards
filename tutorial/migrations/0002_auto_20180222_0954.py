# Generated by Django 2.0.2 on 2018-02-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEularSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionTitle', models.CharField(max_length=250)),
                ('questionSlug', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PythonTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionTitle', models.CharField(max_length=250)),
                ('questionSlug', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameModel(
            old_name='PythonProblem',
            new_name='GolangTutorial',
        ),
    ]
