# Generated by Django 4.2.4 on 2023-08-22 11:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('trial_expiry_date', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('time_zone', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('phone_country_code', models.CharField(blank=True, max_length=6, null=True)),
                ('phone_national_number', models.CharField(blank=True, db_index=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number should not have spaces and special characters: '999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('admin_access_token', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('is_email_validated', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manager.client')),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('client', 'email')},
            },
        ),
    ]