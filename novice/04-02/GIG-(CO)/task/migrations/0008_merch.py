# Generated by Django 2.2 on 2020-09-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20200908_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('kategori', models.CharField(max_length=255)),
                ('harga', models.CharField(max_length=255)),
                ('stock', models.CharField(max_length=255)),
                ('deskripsi', models.TextField(default='')),
            ],
        ),
    ]
