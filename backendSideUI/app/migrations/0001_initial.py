# Generated by Django 3.2.23 on 2024-01-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=70)),
                ('gender', models.CharField(max_length=70)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
