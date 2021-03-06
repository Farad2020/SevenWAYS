# Generated by Django 2.2.6 on 2020-07-17 13:02

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=1000)),
                ('place_phone', models.CharField(blank=True, default='', max_length=100)),
                ('place_address', models.TextField(default='', max_length=100)),
                ('place_building_type', multiselectfield.db.fields.MultiSelectField(choices=[('Residential Buildings', 'Residential Buildings'), ('Educational Buildings', 'Educational Buildings'), ('Institutional Buildings', 'Institutional Buildings'), ('Assembly Buildings', 'Assembly Buildings'), ('Business Buildings', 'Business Buildings'), ('Mercantile Buildings', 'Mercantile Buildings'), ('Industrial Buildings', 'Industrial Buildings'), ('Storage Buildings', 'Storage Buildings'), ('Wholesale Establishments', 'Wholesale Establishments'), ('Hazardous Buildings', 'Hazardous Buildings'), ('Multi-Level Car Parking', 'Multi-Level Car Parking')], default=None, max_length=234)),
                ('place_email', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('working_days', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=56)),
                ('place_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewers_disability_type', multiselectfield.db.fields.MultiSelectField(choices=[('Wheelchair', 'Wheelchair'), ('Powered Wheelchair', 'Powered Wheelchair'), ('Cane Walker', 'Cane Walker')], default=None, max_length=41)),
                ('reviewers_attitude', multiselectfield.db.fields.MultiSelectField(choices=[('Good', 'Good'), ('Tolerable', 'Tolerable'), ('Bad', 'Bad')], default=None, max_length=18)),
                ('reviewers_comment', models.TextField(default='', max_length=700)),
                ('place_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Place')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_img', models.ImageField(default='NULL', upload_to='places_imgs/')),
                ('place_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Place')),
            ],
        ),
    ]
