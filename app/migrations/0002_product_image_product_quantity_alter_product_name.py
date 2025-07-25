# Generated by Django 5.2.1 on 2025-05-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
