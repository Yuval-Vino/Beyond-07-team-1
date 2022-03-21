# Generated by Django 4.0.3 on 2022-03-28 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DogOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=15)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('dog_name', models.CharField(blank=True, max_length=15)),
                ('dog_race', models.CharField(blank=True, max_length=30)),
                ('dog_picture_url', models.CharField(blank=True, max_length=1000)),
                ('dog_age', models.IntegerField(blank=True, null=True)),
                ('dog_weight', models.FloatField(blank=True, null=True)),
                ('dog_gender', models.CharField(blank=True,
                                                choices=[('M', 'Male'), ('F', 'Female'), ('UN', 'Unknown')],
                                                default='UN',
                                                max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
