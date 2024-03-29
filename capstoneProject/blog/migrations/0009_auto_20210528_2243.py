# Generated by Django 3.2.2 on 2021-05-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210528_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('maker', models.CharField(max_length=20)),
                ('shape', models.CharField(max_length=10)),
                ('fcolor', models.CharField(max_length=10)),
                ('bcolor', models.CharField(max_length=10)),
                ('fmark', models.CharField(max_length=10)),
                ('bmark', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='pill_image')),
            ],
        ),
        migrations.AlterField(
            model_name='etcinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='ect_image'),
        ),
        migrations.AlterField(
            model_name='otcinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='otc_image'),
        ),
    ]
