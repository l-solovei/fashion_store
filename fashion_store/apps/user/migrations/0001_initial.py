# Generated by Django 3.2.2 on 2021-05-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('zip', models.CharField(max_length=10, verbose_name='Zip')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is Superuser')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]