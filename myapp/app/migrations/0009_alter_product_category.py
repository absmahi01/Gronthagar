# Generated by Django 4.1.4 on 2022-12-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_payment_paid_payment_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BI', 'Biography'), ('HO', 'Horror'), ('SC', 'Science'), ('KI', 'Kids'), ('HI', 'Historical Fiction'), ('AD', 'Adventure stories'), ('CR', 'Crime')], max_length=2),
        ),
    ]
