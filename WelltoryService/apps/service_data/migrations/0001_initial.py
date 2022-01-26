# Generated by Django 4.0.1 on 2022-01-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('day', models.DateField(auto_now=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
