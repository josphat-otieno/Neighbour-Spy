# Generated by Django 3.2.5 on 2021-07-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spypyapp', '0004_auto_20210725_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_description',
            field=models.TextField(default=''),
        ),
    ]