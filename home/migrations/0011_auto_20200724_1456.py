# Generated by Django 3.0.8 on 2020-07-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_userinfo_r_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='r_url',
            field=models.CharField(max_length=100),
        ),
    ]
