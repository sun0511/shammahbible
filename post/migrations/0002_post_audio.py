# Generated by Django 2.2.6 on 2019-10-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]