# Generated by Django 5.0.4 on 2024-04-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodal',
            name='imagename',
            field=models.CharField(default='randomapp.png', max_length=100),
            preserve_default=False,
        ),
    ]
