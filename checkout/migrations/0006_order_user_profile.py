# Generated by Django 4.1.7 on 2023-03-27 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerprofile', '0005_rename_first_name_customer_name'),
        ('checkout', '0005_remove_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='customerprofile.customer'),
        ),
    ]
