# Generated by Django 4.1.3 on 2023-02-09 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0010_alter_examplemodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c4ba4936-7c17-40bc-9a13-1f65bd7460aa'), primary_key=True, serialize=False),
        ),
    ]