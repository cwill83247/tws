# Generated by Django 4.1.7 on 2023-03-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=200, null=True),
        ),
    ]