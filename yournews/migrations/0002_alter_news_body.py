# Generated by Django 4.2.7 on 2024-03-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yournews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]