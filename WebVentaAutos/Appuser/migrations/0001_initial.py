# Generated by Django 4.1.7 on 2023-04-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
