# Generated by Django 5.0.4 on 2024-04-07 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='employees')),
                ('name', models.CharField(max_length=100)),
                ('job_position', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('bio', models.TextField(max_length=200)),
            ],
        ),
    ]