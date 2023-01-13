# Generated by Django 4.1.2 on 2023-01-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('time', models.TimeField()),
                ('description', models.TextField(max_length=5000)),
            ],
        ),
    ]