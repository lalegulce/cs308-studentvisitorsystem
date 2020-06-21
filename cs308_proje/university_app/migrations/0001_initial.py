# Generated by Django 3.0.4 on 2020-03-25 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('university_address', models.CharField(max_length=200)),
                ('university_contact_number', models.IntegerField()),
                ('university_mail', models.EmailField(max_length=254)),
                ('university_faculties', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UniversitySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_start_date', models.DateTimeField()),
                ('university_end_date', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.University')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityAdmin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=32)),
                ('universiy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.University')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('guide_id', models.AutoField(primary_key=True, serialize=False)),
                ('guide_name', models.CharField(max_length=100)),
                ('guide_faculty', models.CharField(max_length=100)),
                ('universiy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.University')),
            ],
        ),
    ]
