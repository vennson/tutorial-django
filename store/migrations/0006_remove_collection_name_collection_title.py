# Generated by Django 4.1.4 on 2022-12-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20221208_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='name',
        ),
        migrations.AddField(
            model_name='collection',
            name='title',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]