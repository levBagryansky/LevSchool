# Generated by Django 4.1.7 on 2025-04-14 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="added_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
