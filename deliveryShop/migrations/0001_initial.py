# Generated by Django 4.2.2 on 2023-06-06 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=300)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='deliveryShop.shop')),
            ],
        ),
    ]
