# Generated by Django 4.2.3 on 2023-07-31 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_origin', models.CharField(max_length=50)),
                ('total_quantity', models.IntegerField(default=0)),
                ('issued_quantity', models.IntegerField(default=0)),
                ('recieved_quantity', models.IntegerField(default=0)),
                ('unit_price', models.IntegerField(default=0)),
                ('Category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareapp.category')),
            ],
        ),
    ]