# Generated by Django 4.1.3 on 2023-01-19 13:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0004_alter_examplemodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1c2a8d3e-2a0e-49bc-b3b7-f6aa6618015e'), primary_key=True, serialize=False),
        ),
    ]