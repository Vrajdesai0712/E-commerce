# Generated by Django 5.0.1 on 2024-03-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
