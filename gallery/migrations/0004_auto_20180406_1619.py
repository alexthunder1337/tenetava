# Generated by Django 2.0.3 on 2018-04-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_picture_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='size',
            new_name='height',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='filename',
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default=10, upload_to='pictures/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='width',
            field=models.CharField(default=10, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='price',
            field=models.IntegerField(),
        ),
    ]
