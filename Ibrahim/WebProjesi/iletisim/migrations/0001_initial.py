# Generated by Django 3.1 on 2020-08-05 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iletisimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=100)),
                ('soyadi', models.CharField(max_length=100)),
                ('telefon', models.CharField(max_length=10)),
                ('eposta', models.EmailField(max_length=254)),
                ('konu', models.TextField()),
                ('aciklama', models.TextField()),
                ('gonderi_tar', models.DateTimeField(default=django.utils.timezone.now)),
                ('okunma_tar', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
