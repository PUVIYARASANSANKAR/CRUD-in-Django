# Generated by Django 5.0.1 on 2024-01-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=150)),
            ],
        ),
    ]
