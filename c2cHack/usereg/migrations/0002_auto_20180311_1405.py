# Generated by Django 2.0.3 on 2018-03-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usereg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='symps',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='eml',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='pss',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='usr_id',
            field=models.IntegerField(default=129, primary_key=True, serialize=False, unique=True),
        ),
    ]
