# Generated by Django 2.1.7 on 2019-03-04 20:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique_for_date='date'),
            preserve_default=False,
        ),
    ]
