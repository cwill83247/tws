# Generated by Django 4.1.7 on 2023-03-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerprofile', '0002_customer_country_customer_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
