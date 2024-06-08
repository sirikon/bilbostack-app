# Generated by Django 5.0.6 on 2024-06-08 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Speaker",
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
                ("title", models.TextField()),
                ("image", models.ImageField(upload_to="speakers")),
            ],
        ),
        migrations.CreateModel(
            name="Track",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Talk",
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
                ("slug", models.SlugField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("date", models.DateTimeField()),
                ("speakers", models.ManyToManyField(to="venue.speaker")),
                (
                    "track",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="venue.track"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
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
                ("visitor", models.UUIDField()),
                ("rating", models.PositiveSmallIntegerField()),
                ("comment", models.TextField()),
                (
                    "talk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="venue.talk"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("visitor", models.UUIDField()),
                ("question", models.TextField()),
                (
                    "talk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="venue.talk"
                    ),
                ),
            ],
        ),
    ]
