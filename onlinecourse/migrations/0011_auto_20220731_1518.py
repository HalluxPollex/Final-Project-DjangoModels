# Generated by Django 3.2.13 on 2022-07-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0010_auto_20220720_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='id',
        ),
        migrations.AddField(
            model_name='submission',
            name='submission_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
