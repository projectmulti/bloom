# Generated by Django 3.0.9 on 2020-08-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]