# Generated by Django 3.2.5 on 2021-07-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spypyapp', '0003_auto_20210725_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbor',
            name='health_contact',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='neighbor',
            name='police_contact',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]