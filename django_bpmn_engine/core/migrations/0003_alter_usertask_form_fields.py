# Generated by Django 4.0 on 2022-09-22 23:14

from django.db import migrations
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_usertask_form_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='form_fields',
            field=django_jsonform.models.fields.JSONField(blank=True, null=True),
        ),
    ]