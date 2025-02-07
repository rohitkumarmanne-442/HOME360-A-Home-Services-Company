# Generated by Django 5.0.6 on 2024-07-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0012_service_man_available_slots_service_man_total_slots_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_man',
            name='total_slots',
        ),
        migrations.AlterField(
            model_name='service_man',
            name='id_card',
            field=models.FileField(null=True, upload_to='id_cards/'),
        ),
        migrations.AlterField(
            model_name='service_man',
            name='image',
            field=models.FileField(null=True, upload_to='service_man_images/'),
        ),
    ]
