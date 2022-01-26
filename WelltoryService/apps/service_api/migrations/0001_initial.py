# Generated by Django 4.0.1 on 2022-01-26 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='service_api.weightunit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='weight', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
