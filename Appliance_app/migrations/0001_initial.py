# Generated by Django 3.2.7 on 2021-09-25 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=127)),
                ('model', models.CharField(default='', max_length=127)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('inStock', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appliances', to='Appliance_app.category')),
            ],
        ),
    ]
