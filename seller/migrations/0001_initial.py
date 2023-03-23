# Generated by Django 4.0 on 2023-03-23 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('price', models.FloatField(default=0.0)),
                ('sold', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customerseller')),
            ],
        ),
    ]