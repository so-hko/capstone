# Generated by Django 3.2.2 on 2021-05-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210528_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etcinfo',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='otcinfo',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='otcinfo',
            name='nation',
            field=models.CharField(max_length=10),
        ),
    ]