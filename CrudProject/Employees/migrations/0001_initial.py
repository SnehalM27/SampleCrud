# Generated by Django 4.1.5 on 2023-01-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('nm', models.CharField(max_length=30)),
                ('sal', models.FloatField()),
            ],
        ),
    ]
