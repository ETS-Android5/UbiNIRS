# Generated by Django 2.2.5 on 2020-02-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glutentest', '0002_auto_20200206_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='glutentestlog',
            name='trust_flag',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]