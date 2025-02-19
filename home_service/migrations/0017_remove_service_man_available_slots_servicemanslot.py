# Generated by Django 5.0.6 on 2024-07-23 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0016_delete_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_man',
            name='available_slots',
        ),
        migrations.CreateModel(
            name='ServiceManSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('available_slots', models.IntegerField(default=5)),
                ('service_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='home_service.service_man')),
            ],
            options={
                'unique_together': {('service_man', 'date')},
            },
        ),
    ]
