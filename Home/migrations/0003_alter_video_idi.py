# Generated by Django 3.2.4 on 2021-06-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='idi',
            field=models.CharField(max_length=50),
        ),
    ]
