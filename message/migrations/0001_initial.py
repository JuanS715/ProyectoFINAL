# Generated by Django 4.1.3 on 2023-01-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receptor', models.EmailField(max_length=30)),
                ('mensaje', models.TextField(max_length=4000)),
            ],
        ),
    ]
