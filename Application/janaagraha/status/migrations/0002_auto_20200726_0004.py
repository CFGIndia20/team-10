# Generated by Django 3.0.6 on 2020-07-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='user_id',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]