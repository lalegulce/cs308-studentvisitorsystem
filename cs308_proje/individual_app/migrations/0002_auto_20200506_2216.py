# Generated by Django 3.0.5 on 2020-05-06 22:16

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('individual_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
