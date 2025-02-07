from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0007_service_man_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_category',
            name='total',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
