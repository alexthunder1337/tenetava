# Generated by Django 2.0.3 on 2018-04-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_picture_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='price',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]