# Generated by Django 5.1.6 on 2025-02-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
            ],
        ),
    ]
