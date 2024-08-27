# Generated by Django 5.0.7 on 2024-08-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desktop_exe', models.FileField(upload_to='distributions/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
