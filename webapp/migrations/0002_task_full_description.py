# Generated by Django 4.2.7 on 2023-11-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='full_description',
            field=models.TextField(blank=True, null=True, verbose_name='Подробное описание'),
        ),
    ]
