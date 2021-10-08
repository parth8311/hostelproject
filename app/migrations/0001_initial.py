# Generated by Django 2.0 on 2021-08-28 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='abc', max_length=50)),
                ('Lastname', models.CharField(default='abc', max_length=50)),
                ('Contact', models.BigIntegerField(default='123')),
                ('State', models.CharField(default='abc', max_length=50)),
                ('City', models.CharField(default='abc', max_length=50)),
                ('DOB', models.CharField(default='2019-11-11', max_length=50)),
                ('Gender', models.CharField(default='abc', max_length=50)),
                ('Address', models.CharField(default='abc', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='abc', max_length=50)),
                ('Lastname', models.CharField(default='abc', max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(default='abc', max_length=50)),
                ('State', models.CharField(default='abc', max_length=50)),
                ('Gender', models.CharField(default='abc', max_length=50)),
                ('Contact', models.BigIntegerField(default='123')),
                ('DOB', models.CharField(default='2019-11-11', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('ConfirmPassword', models.CharField(default='abc', max_length=50)),
                ('Role', models.CharField(max_length=50)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
