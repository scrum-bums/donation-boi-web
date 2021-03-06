# Generated by Django 2.1.3 on 2018-11-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('location_type', models.CharField(max_length=60)),
                ('website', models.URLField()),
            ],
        ),
    ]
