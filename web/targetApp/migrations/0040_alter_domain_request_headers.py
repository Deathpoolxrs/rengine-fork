# Generated by Django 3.2.4 on 2023-06-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0039_domain_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='request_headers',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
