# Generated by Django 4.1.7 on 2023-03-10 09:25

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('street_address1', models.CharField(max_length=80, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(max_length=40, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('stripe_id', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product')),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-created'], name='checkout_or_created_018c23_idx'),
        ),
    ]