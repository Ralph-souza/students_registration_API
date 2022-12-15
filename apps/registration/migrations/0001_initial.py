from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("id_doc", models.CharField(max_length=15)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Student",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Registration",
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
                ("email", models.EmailField(max_length=250)),
                ("phone", models.CharField(max_length=15)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Masculino"),
                            ("female", "Feminino"),
                            ("other", "Outro(a)"),
                        ],
                        default=None,
                        max_length=50,
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("fundamental", "Fundamental completo"),
                            ("fundamental_na", "Fundamental incompleto"),
                            ("high_school", "Ensino medio completo"),
                            ("high_school_na", "Ensino medio incompleto"),
                            ("graduation", "Superior completo"),
                            ("graduation_na", "Superio incompleto"),
                            ("other", "Outro"),
                        ],
                        default=None,
                        max_length=50,
                    ),
                ),
                (
                    "relationship",
                    models.CharField(
                        choices=[
                            ("father", "Pai"),
                            ("mother", "Mae"),
                            ("other", "Outro"),
                        ],
                        default=None,
                        max_length=50,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registration.student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registration",
            },
        ),
    ]
