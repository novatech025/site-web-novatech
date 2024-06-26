# Generated by Django 4.2.8 on 2024-04-12 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('content', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='images/services')),
            ],
        ),
    ]
