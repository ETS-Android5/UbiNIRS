# Generated by Django 2.2.5 on 2019-11-24 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_appspectrumfile_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='appspectrumfile',
            name='app',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.UbiNIRSApp'),
        ),
    ]