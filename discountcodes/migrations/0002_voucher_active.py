# Generated by Django 4.1.7 on 2023-03-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountcodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
