# Generated by Django 5.1.4 on 2024-12-12 15:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="sulg",
            new_name="slug",
        ),
    ]
