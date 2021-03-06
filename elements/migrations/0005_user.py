# Generated by Django 2.2.2 on 2019-06-13 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0004_auto_20190610_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, default='', null=True)),
                ('last_name', models.TextField(blank=True, default='', null=True)),
                ('username', models.TextField(blank=True, default='', null=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.TextField(blank=True, default='', null=True)),
                ('password', models.CharField(default='', max_length=100)),
                ('password2', models.CharField(default='', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
