# Generated by Django 2.2.3 on 2019-09-10 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190829_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 9, 19, 1, 434994), verbose_name='date published'),
        ),
    ]