# Generated by Django 4.2.4 on 2023-08-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_comment_user_alter_event_date_alter_event_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default='2023-08-17', verbose_name='Party Date'),
        ),
    ]
