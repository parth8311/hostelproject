# Generated by Django 2.0 on 2021-08-28 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(default='abc', max_length=50)),
                ('State', models.CharField(default='abc', max_length=50)),
                ('City', models.CharField(default='abc', max_length=50)),
                ('Image', models.ImageField(upload_to='imag/')),
                ('Roomno', models.BigIntegerField(default='1')),
                ('Rent', models.CharField(default='1000', max_length=50)),
                ('AC', models.CharField(default='abc', max_length=50)),
                ('Gender', models.CharField(default='abc', max_length=50)),
                ('Speciality', models.CharField(default='abc', max_length=500)),
                ('Food', models.CharField(default='abc', max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Owner')),
            ],
        ),
    ]
