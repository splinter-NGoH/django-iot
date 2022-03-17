# Generated by Django 3.2.12 on 2022-03-17 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
        ('iotdevices', '0002_auto_20220317_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices_in_room', to='rooms.room'),
        ),
    ]
