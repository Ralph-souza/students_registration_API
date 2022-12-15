from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="contact_name",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="contact_number",
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
