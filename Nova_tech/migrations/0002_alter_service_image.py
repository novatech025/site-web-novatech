# Generated by Django 4.2.8 on 2024-04-12 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nova_tech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/services'),
        ),
    ]