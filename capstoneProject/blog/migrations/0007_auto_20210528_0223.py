# Generated by Django 3.2.2 on 2021-05-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210526_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etcinfo',
            name='name',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='otcinfo',
            name='name',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
