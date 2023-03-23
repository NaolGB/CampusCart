# Generated by Django 4.0 on 2023-03-23 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register_login', '__first__'),
        ('seller', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register_login.customerseller')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.items')),
            ],
        ),
    ]
