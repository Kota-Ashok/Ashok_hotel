# Generated by Django 5.0.2 on 2024-03-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_form',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_purchase', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('items', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
