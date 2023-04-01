# Generated by Django 4.1.7 on 2023-04-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dispatched_by',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_dispatched',
            field=models.BooleanField(default=False),
        ),
    ]
