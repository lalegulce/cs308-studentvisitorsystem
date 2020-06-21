# Generated by Django 3.0.5 on 2020-04-27 19:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('individual_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('mail', models.EmailField(max_length=254)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
    ]
