# Generated by Django 4.2.15 on 2024-08-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attend", "0005_auto_20210501_0312"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
