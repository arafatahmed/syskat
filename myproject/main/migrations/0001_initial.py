# Generated by Django 5.1.4 on 2024-12-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=50)),
                ('fb', models.CharField(max_length=50)),
                ('tw', models.CharField(max_length=50)),
                ('yt', models.CharField(max_length=50)),
                ('tell', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('set_name', models.CharField(max_length=50)),
            ],
        ),
    ]
