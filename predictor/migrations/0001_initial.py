from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="PredictionHistory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("description", models.CharField(max_length=255)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("payment_method", models.CharField(max_length=80)),
                ("location", models.CharField(max_length=80)),
                ("account_type", models.CharField(max_length=80)),
                ("device_used", models.CharField(max_length=80)),
                ("merchant_type", models.CharField(max_length=80)),
                ("loyalty_program", models.CharField(max_length=8)),
                ("time_of_day", models.CharField(max_length=40)),
                ("transaction_date", models.DateField()),
                ("predicted_category", models.CharField(max_length=100)),
            ],
            options={"ordering": ["-created_at"]},
        )
    ]
