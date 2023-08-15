# Generated by Django 4.2.4 on 2023-08-15 20:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_event_map_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attending_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='sport',
            field=models.CharField(choices=[('Football', 'Football'), ('Basketball', 'Basketball'), ('Baseball', 'Baseball')], default='Football', max_length=100),
        ),
    ]