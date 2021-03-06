# Generated by Django 2.1.5 on 2019-02-21 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('misc', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=32)),
                ('chinese_name', models.CharField(max_length=32)),
                ('access_user_id', models.CharField(blank=True, db_index=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('roles', models.ManyToManyField(to='misc.Role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=64, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
                ('roles', models.ManyToManyField(to='misc.Role')),
            ],
        ),
    ]
