# Generated by Django 3.0.1 on 2020-02-16 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wpisy', '0004_auto_20200215_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='wpis',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
