# Generated by Django 5.0.7 on 2024-09-12 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-created_at'], 'verbose_name': 'Application', 'verbose_name_plural': 'Applications'},
        ),
    ]