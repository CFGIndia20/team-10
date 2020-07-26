# Generated by Django 3.0.8 on 2020-07-26 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaints', '0004_auto_20200726_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL),
        ),
    ]
