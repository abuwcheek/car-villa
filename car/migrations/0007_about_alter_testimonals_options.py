# Generated by Django 5.1.1 on 2024-10-21 17:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_testimonals'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=100)),
                ('phone_numara', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=100)),
                ('youtube', models.CharField(max_length=500)),
                ('telegram', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='testimonals',
            options={'verbose_name': 'Testimonal', 'verbose_name_plural': 'Testimonals'},
        ),
    ]