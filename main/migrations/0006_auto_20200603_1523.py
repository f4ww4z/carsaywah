# Generated by Django 3.0.6 on 2020-06-03 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20200526_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='car_id',
            new_name='car',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='owner',
            new_name='renter',
        ),
        migrations.AddField(
            model_name='car',
            name='bookedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_bookedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]