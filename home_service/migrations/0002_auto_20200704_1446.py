from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_man',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_man',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_man',
            name='id_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Total_Man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.Service')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.Service_Category'),
        ),
        migrations.AddField(
            model_name='service',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.Service_Man'),
        ),
    ]
