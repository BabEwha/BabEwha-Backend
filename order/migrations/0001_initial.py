# Generated by Django 5.0.3 on 2024-03-16 20:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("groups", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("is_order_active", models.BooleanField(default=True)),
                (
                    "order_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="order/%Y/%m/%d"
                    ),
                ),
                ("order_time", models.DateTimeField(auto_now_add=True)),
                ("order_status", models.CharField(max_length=100)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="groups.group"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "order",
            },
        ),
        migrations.CreateModel(
            name="OrderDetail",
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
                ("menu", models.TextField()),
                ("price", models.IntegerField()),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="order.order"
                    ),
                ),
            ],
            options={
                "db_table": "orderdetail",
            },
        ),
    ]
