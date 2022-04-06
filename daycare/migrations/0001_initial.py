# Generated by Django 4.0.3 on 2022-04-03 13:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, unique=True,
                                          validators=[django.core.validators.MaxLengthValidator])),
                ('description', models.TextField(blank=True, null=True)),
                ('price_per_day', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(blank=True)),
                ('area', models.CharField(blank=True, max_length=20,
                                          validators=[django.core.validators.MaxLengthValidator])),
                ('city', models.CharField(blank=True, max_length=20,
                                          validators=[django.core.validators.MaxLengthValidator])),
                ('address', models.CharField(blank=True, max_length=50,
                                             validators=[django.core.validators.MaxLengthValidator])),
                ('user', models.OneToOneField(blank=True, default=None,
                                              on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]