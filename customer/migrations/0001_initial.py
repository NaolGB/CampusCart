# Generated by Django 4.0 on 2023-03-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('role', models.CharField(choices=[('CR', 'Customer'), ('SR', 'Seller')], default='CR', max_length=2)),
            ],
        ),
    ]
