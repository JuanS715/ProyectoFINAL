# Generated by Django 4.1.3 on 2023-01-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
