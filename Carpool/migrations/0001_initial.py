# Generated by Django 3.1.2 on 2020-11-03 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('driver_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('car_plate', models.CharField(max_length=8, unique=True)),
                ('car_model', models.CharField(max_length=32)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'drivers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Riders',
            fields=[
                ('rider_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'riders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('timeslot', models.TimeField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'time',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('email_address', models.CharField(max_length=32, unique=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Carpool.drivers')),
                ('driver_firstname', models.CharField(blank=True, max_length=32, null=True)),
                ('driver_lastname', models.CharField(blank=True, max_length=32, null=True)),
                ('car_model', models.CharField(blank=True, max_length=32, null=True)),
                ('driver_rating', models.IntegerField(blank=True, null=True)),
                ('rider_firstname', models.CharField(blank=True, max_length=32, null=True)),
                ('rider_lastname', models.CharField(blank=True, max_length=32, null=True)),
                ('rider_rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'requests',
                'managed': False,
            },
        ),
    ]
