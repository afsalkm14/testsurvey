# Generated by Django 3.2.7 on 2021-09-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('utype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('pregnancy', models.CharField(max_length=20)),
                ('marital', models.CharField(max_length=20)),
                ('diet', models.CharField(max_length=20)),
                ('ratefollow', models.CharField(max_length=20)),
                ('rate', models.CharField(max_length=20)),
                
            ],
        ),
    ]
