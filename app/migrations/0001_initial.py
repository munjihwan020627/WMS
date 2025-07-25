# Generated by Django 5.2.1 on 2025-05-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer", models.CharField(max_length=200)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("products", models.ManyToManyField(to="app.product")),
            ],
        ),
    ]
