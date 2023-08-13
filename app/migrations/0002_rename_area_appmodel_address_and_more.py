# Generated by Django 4.2.3 on 2023-07-31 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appmodel',
            old_name='area',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='appmodel',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='appmodel',
            old_name='mobilenumber',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='appmodel',
            name='lastname',
        ),
        migrations.AddField(
            model_name='appmodel',
            name='join',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='appmodel',
            table='APPMODEL',
        ),
    ]
