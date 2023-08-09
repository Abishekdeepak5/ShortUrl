# Generated by Django 4.2.4 on 2023-08-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.CharField(max_length=500)),
                ('shorturl', models.CharField(max_length=7)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
