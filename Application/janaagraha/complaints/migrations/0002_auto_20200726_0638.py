# Generated by Django 3.0.8 on 2020-07-26 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='complaints'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='userid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]